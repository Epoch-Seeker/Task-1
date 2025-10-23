 ## Overview
This project demonstrates running a **Pathway program** inside a **Docker container** on a Windows machine. Since Pathway only supports Linux environments, Docker ensures a consistent environment for everyone.

---

## Files
- `sample_pathway.py` – A minimal Pathway program that prints a message.  
- `Dockerfile` – Defines the container environment for running the Pathway program.  
- `requirements.txt` – Lists Python dependencies (`pathway`).

---

## Setup Instructions

1. **Install Docker Desktop**  
   Download and install: [Docker Desktop](https://www.docker.com/products/docker-desktop/)  
   Make sure WSL 2 is enabled.

2. **Build the Docker Image**
```bash
docker build -t pathway-sample .
```

3. **Run the Docker Container**
```bash
docker run --rm pathway-sample
```
You should see the output:
```bash
Hello from Pathway inside Docker!
```