# ${{ values.name }}

${{ values.description }}

Scaffolded from the **Python App** template. On every push to `main`, CI builds a
container image and Argo CD deploys it to Kubernetes automatically.

| Path | Purpose |
|------|---------|
| `src/` | Application source (Flask app on port 5000) |
| `Dockerfile` | Container build |
| `charts/app/` | Helm chart deployed by Argo CD |
| `.github/workflows/cicd.yaml` | Build → push image → bump chart → sync Argo CD |
| `docs/` | TechDocs (mkdocs) |

Owned by `${{ values.owner }}`.
