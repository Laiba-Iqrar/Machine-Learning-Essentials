# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install required Python packages
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Install Jupyter Notebook
RUN pip install notebook

# Expose the default Jupyter Notebook port
EXPOSE 8888

# Start the Jupyter Notebook server
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
