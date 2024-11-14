<d align="center">
  <h1><strong>Prototype JSON:API</strong></h1>
</d>

## 📄 Output Example

```json
{
	"data": [
		{
			"type": "Automobile",
			"id": "663974ff-0e02-4ec8-9417-50092c73909e",
			"attributes": {
				"is_available": true,
				"created_at": "2024-11-14T16:54:54.982701Z",
				"updated_at": "2024-11-14T16:54:54.982701Z",
				"model": "Corolla",
				"year": 2020,
				"serial_number": "SN1234567890",
				"role": "available",
				"daily_rate": "35.50"
			},
			"relationships": {
				"make_id": {
					"data": {
						"type": "Make",
						"id": "5ab56f78-276d-469d-8ae3-4558a88d8387"
					}
				},
				"location": {
					"data": {
						"type": "Location",
						"id": "6254ec53-56cc-4088-9cee-dc460aaae45b"
					}
				}
			}
		}
	]
}
```

## ⚙️ Installation

Clone the repository.

```bash
git clone git@github.com:tyronejosee/prototype_json_api.git
```

Create a virtual environment (Optional, only if you have Python installed).

```bash
python -m venv env
```

Activate the virtual environment (Optional, only if you have Python installed).

```bash
env\Scripts\activate
```

> Notes: `(env)` will appear in your terminal input.

Install all dependencies (Optional, only if you have Python installed).

```bash
pip install -r requirements/local.txt
```

Create a copy of the `.env.example` file and rename it to `.env`.

```bash
cp .env.example .env
```

**Update the values of the environment variables (Important).**

> Note: Make sure to correctly configure your variables before building the container.

## 🐍 Django

Create the migrations.

```bash
python manage.py makemigrations
```

Run the migrations.

```bash
python manage.py migrate
```

If you need to be more specific, use:

```bash
python manage.py migrate <app_label> <migration_name>
```

List all available migrations and their status.

```bash
python manage.py showmigrations
```

> Note: Manually create the migration if Django skips an app; this happens because Django did not find the `/migrations` folder.

Create a superuser to access the entire site without restrictions.

```bash
python manage.py createsuperuser
```

Log in to `admin`:

```bash
http://127.0.0.1:8000/admin/
```

Access Swagger or Redoc.

```bash
http://127.0.0.1:8000/api/schema/swagger/
http://127.0.0.1:8000/api/schema/redoc/
```

## 🚨 Important Notes

Check the creation of migrations before creating them.

```bash
python manage.py makemigrations users
```

> Note: Checking migrations before their creation is necessary to avoid inconsistencies in user models.

## ⚖️ License

This project is under the [Apache-2.0 license](https://github.com/tyronejosee/prototype_json_api/blob/main/LICENSE).
