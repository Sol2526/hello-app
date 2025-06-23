$imageN = "sol2526/hello-app"
$containerN = "hello-app"
#script is to automate the re-deployment of a docker container with a new image
Write-Host "Stopping container if running.."
docker stop $containerN 2>$null
Write-Host "Removing old container if any.."
docker rm $containerN 2>$null
Write-Host "Pulling the latest image.."
docker pull $imageN
Write-Host "Starting app.."
docker run -d -p 5000:5000 --name $containerN $imageN
Write-Host "Visit localhost:5000 to view running app"