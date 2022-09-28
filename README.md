# Thyroid-Disease-Detection


## Heroku link
### https://thyroiddiseasedetect.herokuapp.com/

**click this**<br>
[Thyroid-Disease-Detection](https://thyroiddiseasedetect.herokuapp.com/)



### Docker Image

    FROM python:3.10
    COPY . /app
    WORKDIR /app
    RUN pip install -r requirements.txt
    EXPOSE $PORT
    CMD gunicore --workers=4 --bind 0.0.0.0:$PORT aap:app
    
    
### Procfile
    web gunicorn app:app

### Screenshot

*
![Capture](https://user-images.githubusercontent.com/84202477/192757330-93833a1b-da83-4e22-ae46-17ad3f094fa1.PNG)
