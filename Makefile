run:
	docker compose up --build

stop:
	docker compose down

clean:
	docker compose down -v --rmi all

logs:
	docker compose logs -f app

restart:
	docker compose down && docker compose up --build
