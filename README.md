# Student Pass/Fail Predictor — Docker deployment

Flask + scikit-learn sample app for the MLOps practical assessment.

## Project files

- `train.py`: creates sample student data, trains the model, saves `student_model.pkl`.
- `app.py`: Flask web app for Pass/Fail prediction.
- `templates/index.html`: HTML form.
- `requirements.txt`: Python dependencies.
- `Dockerfile`: installs dependencies, trains the model during image build, and starts Flask.

## Build and run locally or on Ubuntu EC2

From the folder containing the Dockerfile:

```bash
docker build -t student-app .
docker run -d --name student-app --restart unless-stopped -p 80:5000 student-app
```

Open `http://localhost` locally, or `http://YOUR-EC2-PUBLIC-IP` on EC2 after allowing inbound HTTP (TCP 80) in the EC2 security group.

If port 80 is already occupied, stop/remove the old `student-app` container before rerunning. To inspect logs:

```bash
docker ps -a
docker logs student-app
```

The model is generated from demonstration data; this is not a real student grading policy.
