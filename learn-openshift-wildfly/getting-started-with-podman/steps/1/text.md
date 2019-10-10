
One of the simplest examples could be running an HelloWorld container.

The CLI for Podman is compatible with Docker, meaning it should feel familiar. For example, if you were to build a new image, you can use a Dockerfile and build it using podman build command. For example:

```cat > Dockerfile <<EOF
FROM fedora:28
RUN dnf -y install cowsay
EOF```{{execute}}


Now build the image with:
`podman build . -t hello-world`{{execute}}

