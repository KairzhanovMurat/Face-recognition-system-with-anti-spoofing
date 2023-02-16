from django.shortcuts import render
from django.views import generic
from .forms import UserForm
from django.shortcuts import redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth import get_user_model
from rest_framework import generics, authentication, permissions
from .serializers import CreateUserSerializer, TokenAuthSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


# Create your views here.
class Register(generic.TemplateView):
    template_name = 'registration.html'

    def get_context_data(self, **kwargs):
        ctxt = super(Register, self).get_context_data()
        ctxt['form'] = UserForm
        return ctxt

    def post(self, request):
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            name = form.cleaned_data.get('name')
            image = form.cleaned_data.get('face_image')
            get_user_model().objects.create_user(
                password=password, email=email,
                name=name, face_image=image)

            user = authenticate(password=password, email=email)
            login(request, user)
            return redirect('base:home')

        else:
            context = {'form': form}
        return render(request, self.template_name, context=context)


class Home(generic.TemplateView):
    template_name = 'main_page.html'


class UpdateProfileView(generic.UpdateView):
    template_name = 'update_profile.html'
    model = get_user_model()
    fields = ('face_image', 'name',)

    def get_success_url(self):
        return reverse('base:home')


### API related views ###


class CreateUserView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer


class CreateTokenView(ObtainAuthToken):
    serializer_class = TokenAuthSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUsersView(generics.RetrieveUpdateAPIView):
    serializer_class = CreateUserSerializer
    authentication_classes = [authentication.TokenAuthentication, ]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
