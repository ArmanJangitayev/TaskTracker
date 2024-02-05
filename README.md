# Аутентификация и Авторизация:
### Реализовал систему регистрации и входа пользователей с использованием email и пароля. 
Во users/views.py: class Register
 и создал форму в forms.py:class RegisterForm(UserCreationForm) с ссылкой на родительский встроенный класс, class LoginForm(AuthenticationForm): с ссылкой на родительский встроенный класс.
Так же дабавил аутентифкацию, независимо от ввода емаил или логина, будет корректно аутентифицировать! Реализация была в users/backends.py: class EmailBackend(ModelBackend): где функционал работает функцию authenticate и проверки try/except.

В urlpatterns, добавил встроенную сслыку на аутентификацию и указал ссылку register/.

    - urlpatterns = [
      path('', include('django.contrib.auth.urls')),

      path('register/', Register.as_view(), name='register'),

]
  - Организовать механизм аутентификации и авторизации с использованием сессий и cookies. 
  - Так как  механизм аутентификации и авторизации с использованием сессий и cookies уже по умолчанию, реализован, только проверили, по sessionid по юзеру в БД, и inspect elements(улитилита разработчика сайта(Safari)) 
# Создание, Редактирование и Удаление Задач:
### Разработать интерфейс для добавления новых задач, включая описание и срок выполнения.
### Обеспечить возможность редактирования и удаления созданных задач
  - Использовал для реализации встроенный классы как: 
    -       class TaskListView(ListView):с ссылкой на базовый класс:
                model = Task
                template_name = 'tasks/list.html'

                    def get_object(self, queryset=None):
                        if queryset is not None:
                            return queryset.objects.get(pk=self.kwargs['pk'])
                        return None

#### Реализация поиска 
    def get_queryset(self):
        queryset = super(TaskListView, self).get_queryset()
        search_query = self.request.GET.get('search', False)
        if search_query:
            queryset = queryset.filter(title__icontains=search_query, description__icontains=search_query)
        return queryset 
#### Реализация внутренней сортивочной выборки : To Do, Doing, Done.
    def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        queryset = self.get_queryset()
        context['todo_tasks'] = queryset.filter(status=Task.TODO).all()

        context['in_progress_tasks'] = queryset.filter(status=Task.IN_PROGRESS).all()

        context['done_tasks'] = queryset.filter(status=Task.COMPLETED).all()
        return context

#### Использование родительского класса для наследования:
    class TaskCreateView(CreateView):
        model = Task
        template_name = 'tasks/create.html'
        form_class = TaskCreateForm
        queryset = Task.objects.all()

    def get_success_url(self):
        return reverse_lazy('tasks')


    class TaskUpdateView(LoginRequiredMixin, UpdateView):
        model = Task
        template_name = 'tasks/update.html'
        form_class = TaskUpdateForm
        queryset = Task.objects.all()

    def get_success_url(self):
        return reverse_lazy('tasks')


    class TaskDeleteView(DeleteView):
        model = Task
        success_url = reverse_lazy('tasks')

#### Создание API for Tasks

    class TasksViewAPI(ListAPIView, CreateAPIView):
        queryset = Task.objects.all()
        serializer_class = TaskSerializer


    class TasksViewDetailAPI(UpdateAPIView, DestroyAPIView, RetrieveAPIView):
        queryset = Task.objects.all()
        serializer_class = TaskSerializer

#### В файле serializers реализован:
    class TaskSerializer(serializers.ModelSerializer):
        class Meta:
            model = Task
            fields = '__all__'

#### Это  формы: которые реализованы для Созадния и Обновления Task.
    class TaskCreateForm(forms.ModelForm):
        class Meta:
            model = Task
            fields = '__all__'


    class TaskUpdateForm(forms.ModelForm):
        class Meta:
            model = Task
            fields = '__all__'

### После Мигрировал на базу PostgreSQl, развернутую на docker, но так как мы выгружали на pythonanywhere, я вернулся на Sqlite3.

# Отметка Выполненных Задач:
  - Ввести механизм отметки задач как выполненных, с возможностью их отображения.
Так как мы ввели ввыборку To Do, Doing ,Done, у нас есть возможность менять статус задачи и назначать описание и дату и присваивать юзера.

# Работа с  медиафайлами
#### Реализовал в модельке class Task(models.Model)
##### Где инициализировал поле медиа: так же медиа сохранятется: и отправляется в базу!
