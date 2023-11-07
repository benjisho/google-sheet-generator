FROM nginx:latest

# Remove the default Nginx configuration file
RUN rm /etc/nginx/conf.d/default.conf

# Copy a new configuration file from the current directory
COPY nginx.conf /etc/nginx/nginx.conf

# Expose ports
EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]
