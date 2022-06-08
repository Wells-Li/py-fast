DEBUGIMAGE_TAG = py-fast-v1
DEBUGIMAGE = wellsli/tools:$(DEBUGIMAGE_TAG)

WORKDIR = /mnt/py-fast

deploy_dev:
	docker pull $(DEBUGIMAGE)
	docker run \
		-it \
		--rm \
		--name fastapi \
		-p 18088:18088 \
		-v $$PWD:$(WORKDIR) \
		-w $(WORKDIR) \
		$(DEBUGIMAGE) \
		/bin/bash
