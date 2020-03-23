# Environment Setup Tutorial

## Install Python 3.8, Virtual Environments, Django 3+ on Windows using virtualenv, pip and Windows Powershell

Detailed setup can be found in https://www.codingforentrepreneurs.com/blog/install-python-django-on-windows/.

### 1. Download Python from https://www.python.org/downloads/

### 2. Verify Python Installed in Powershell

Type `python -V` and check if the following shows up:

```
Python 3.8.2
```

Verify pip by entering:

```
pip freeze
```

 If you see `The term 'pip' is not recognized as the name...` then you do the installation correctly. Otherwise, you're good. 

### 3. Go to your Developing Folder using CMD or Powershell

### 4. Install `Virtualenv`

1.  To install a `Pipenv` as our virtual environment manager: 

```
pip install virtualenv
```

> Tips: 国内开发者建议换 pip镜像源。使用以下命令行：
>
> ```
> > pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
> ```

2. Verify:

```
> pip freeze
virtualenv==16.7.9
```

### 5. Create a Virtualenv:

1. Go to the project's parent directory. In my case:

   ```
   > cd D:\CPS\Course\Capstone\Diet_Master
   ```

2. Make a new directory called `venv`.

   ```
   [my-project-location]> mkdir venv
   ```

3. Create `virtualenv`:

   ```
   > virtualenv ./venv
   ```

3. Make sure you enable "Run as Administrator" before moving forward.
   Verify by

   ```
   Set-ExecutionPolicy Unrestricted
   ```

4. Activate your environment:

   ```
   > ./venv/Scripts/activate
   ```

5. Done! Verify it:

    ```
    (venv) > pip freeze
    ```

	- `pip freeze`  should return nothing at this point 

### 6. Activate and Deactivate Virtualenv

```
> cd ~\Dev\cfehome # or your virtualenv's path
> .\venv\Scripts\activate
(venv) > deactivate
> .\venv\Scripts\activate
(venv) >
```

### 7. Install Django Package

```
(venv) > pip install django==3.0.2
```

Verify by `pip freeze`

```
asgiref==3.2.5
Django==3.0.2
pytz==2019.3
sqlparse==0.3.1
```

### 8. That's it! You can run server using

```
(venv) > python manage.py runserver
```

Your can start the development server at `http://127.0.0.1:8000`