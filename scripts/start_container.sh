
#!/bin/bash
set -e

cd /home/ubuntu/student-predictor

docker build -t student-predictor:latest .

docker run -d \
  --name student-predictor \
  --restart unless-stopped \
  -p 80:5000 \
  student-predictor:latest
