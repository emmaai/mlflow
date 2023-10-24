# Enable Nginx
- enable 80 in security group settings of ec2 instance
- copy `reverse_proxy.conf` to `/etc/nginx/sites-enabled`
- change `server_name` to your host name (if dns enabled) or ip

# Build MLflow docker image
`docker build . -t mlflow:test` change the name and tag if you prefer

# Run MLflow server
`docker-compose up`

# Use MLflow to track your experiments
See `example.py` presumably 
- you have write access to aws s3 and config the credential correctly
- the experiment is run on the same ec2 instance
