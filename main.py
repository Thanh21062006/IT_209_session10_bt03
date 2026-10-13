import subprocess

def run_command(command):
    print(f"Executing: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)

if __name__ == '__main__':
    print("Starting Docker build automation script...")
    run_command("docker build -t hw-backend:single -f Dockerfile.single .")
    run_command("docker build -t hw-backend:multistage -f Dockerfile .")
    run_command("docker images | grep hw-backend")