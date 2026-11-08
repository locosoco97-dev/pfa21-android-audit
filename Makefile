# PFA-21 - commandes du cycle setup / start / test / stop
IMAGE ?= pfa21-audit
RUN   := docker run --rm -v "$(CURDIR)":/work $(IMAGE)

.PHONY: setup start test stop clean

setup:   ## Construit l image et verifie l environnement
	docker build -t $(IMAGE) .
	$(RUN) python scripts/check_env.py

start:   ## Lance l audit (disponible a partir du Sprint 3)
	@if [ -f src/audit.py ]; then $(RUN) python src/audit.py manifests/avant/AndroidManifest.xml --json preuves/rapport_avant.json; \
	else echo "[start] src/audit.py absent : prevu au Sprint 3"; fi

test:    ## Lance la suite de tests
	$(RUN) pytest -q

stop:    ## Nettoie conteneurs orphelins et fichiers temporaires
	-@docker ps -aq --filter ancestor=$(IMAGE) | xargs -r docker rm -f
	@find . -name __pycache__ -type d -prune -exec rm -rf {} + 2>/dev/null; rm -rf .pytest_cache
	@echo "[stop] nettoyage termine"

clean: stop ## Supprime aussi l image Docker
	-docker image rm $(IMAGE)
