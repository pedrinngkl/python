'''agora vamos criar um curriculo usando o decorators para organizar as informações de forma clara e elegante.'''

from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/curriculo')
def curriculo():
    html_content = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Currículo Premium | Pedro Gonçalves</title>
        <link href="https://googleapis.com" rel="stylesheet">
        <style>
            :root {{
                --primary: #6366f1;
                --secondary: #a855f7;
                --bg: #0f172a;
                --card: #1e293b;
                --text: #f8fafc;
                --text-dim: #94a3b8;
            }}

            body {{
                font-family: 'Inter', sans-serif;
                background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
                color: var(--text);
                margin: 0;
                padding: 50px 20px;
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
            }}

            .container {{
                width: 100%;
                max-width: 1000px;
                background: rgba(30, 41, 59, 0.7);
                backdrop-filter: blur(12px);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 24px;
                overflow: hidden;
                display: grid;
                grid-template-columns: 320px 1fr;
                box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            }}

            /* Sidebar */
            .sidebar {{
                background: rgba(15, 23, 42, 0.5);
                padding: 40px;
                border-right: 1px solid rgba(255, 255, 255, 0.05);
            }}

            .profile-pic {{
                width: 100px;
                height: 100px;
                background: linear-gradient(45deg, var(--primary), var(--secondary));
                border-radius: 20px;
                margin-bottom: 20px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 2.5rem;
                font-weight: 800;
            }}

            .sidebar h2 {{
                font-size: 0.8rem;
                text-transform: uppercase;
                letter-spacing: 0.15rem;
                color: var(--primary);
                margin: 30px 0 15px;
            }}

            .contact-info p {{
                font-size: 0.9rem;
                color: var(--text-dim);
                margin: 8px 0;
            }}

            .skill-list {{
                display: flex;
                flex-wrap: wrap;
                gap: 8px;
            }}

            .skill-badge {{
                background: rgba(99, 102, 241, 0.1);
                border: 1px solid rgba(99, 102, 241, 0.2);
                color: #c7d2fe;
                padding: 6px 12px;
                border-radius: 8px;
                font-size: 0.75rem;
                font-weight: 600;
            }}

            /* Main Content */
            .main-content {{
                padding: 50px;
            }}

            header h1 {{
                font-size: 3rem;
                font-weight: 800;
                margin: 0;
                background: linear-gradient(to right, #fff, #94a3b8);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }}

            header p {{
                font-size: 1.2rem;
                color: var(--secondary);
                font-weight: 600;
                margin: 5px 0 40px;
            }}

            .section-title {{
                font-size: 1.25rem;
                font-weight: 700;
                margin-bottom: 25px;
                display: flex;
                align-items: center;
                gap: 10px;
            }}

            .section-title::after {{
                content: "";
                height: 1px;
                flex: 1;
                background: rgba(255, 255, 255, 0.1);
            }}

            .experience-card {{
                background: rgba(255, 255, 255, 0.03);
                border: 1px solid rgba(255, 255, 255, 0.05);
                padding: 25px;
                border-radius: 16px;
                transition: transform 0.3s ease;
            }}

            .experience-card:hover {{
                transform: translateY(-5px);
                background: rgba(255, 255, 255, 0.05);
            }}

            .experience-card h3 {{
                margin: 0;
                color: var(--text);
                font-size: 1.1rem;
            }}

            .experience-card .meta {{
                color: var(--primary);
                font-size: 0.85rem;
                font-weight: 600;
                margin: 5px 0 15px;
            }}

            .experience-card p {{
                color: var(--text-dim);
                font-size: 0.95rem;
                line-height: 1.6;
                margin: 0;
            }}

            @media (max-width: 850px) {{
                .container {{ grid-template-columns: 1fr; }}
                .sidebar {{ border-right: none; border-bottom: 1px solid rgba(255,255,255,0.1); }}
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <aside class="sidebar">
                <div class="profile-pic">PG</div>
                <div class="contact-info">
                    <h2>Contato</h2>
                    <p>📧 pedrogpereira9@gmail.com</p>
                    <p>📍 Belo Horizonte, MG</p>
                </div>

                <h2>Tech Stack</h2>
                <div class="skill-list">
                    <div class="skill-badge">AWS (Cloud)</div>
                    <div class="skill-badge">Docker</div>
                    <div class="skill-badge">Kubernetes</div>
                    <div class="skill-badge">Python</div>
                    <div class="skill-badge">Flask</div>
                    <div class="skill-badge">Prometheus</div>
                    <div class="skill-badge">Grafana</div>
                    <div class="skill-badge">CI/CD</div>
                </div>

                <h2>Educação</h2>
                <p style="font-size: 0.9rem; color: var(--text);">
                    <strong>Técnico em Informática</strong><br>
                    <span style="color: var(--text-dim)">Cotemig</span>
                </p>
            </aside>

            <main class="main-content">
                <header>
                    <h1>Pedro Gonçalves</h1>
                    <p>DevOps Júnior</p>
                </header>

                <section>
                    <div class="section-title">Experiência</div>
                    <div class="experience-card">
                        <h3>Estagiário em DevOps</h3>
                        <div class="meta">CONTRUSITE BRASIL | 2025 - PRESENTE</div>
                        <p>
                            Focado na modernização de infraestrutura. Atuação direta com gerenciamento de containers em Docker, 
                            provisionamento em AWS e estruturação de observabilidade com Prometheus e dashboards no Grafana.
                        </p>
                    </div>
                </section>
            </main>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)




