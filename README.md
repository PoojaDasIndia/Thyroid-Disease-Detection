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
![Screenshot](https://user-images.githubusercontent.com/84202477/192740131-a2563039-91f1-47f0-9ce5-3f8e1c340cf9.PNG)
