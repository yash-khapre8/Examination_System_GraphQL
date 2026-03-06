from flask import Flask, request, jsonify
from flask_cors import CORS
from database import db
from config import Config
from schema.schema import schema

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    
    db.init_app(app)
    
    with app.app_context():
        # Import models to ensure they are registered
        import models
        db.create_all()

    @app.route('/', methods=['GET'])
    def index():
        return jsonify({
            "message": "Online Examination System API is running",
            "graphql_endpoint": "/graphql"
        })

    @app.route('/graphql', methods=['GET', 'POST'])
    def graphql_server():
        if request.method == 'GET':
            # Updated to use more stable CDN links and include necessary CSS
            return f'''
            <!DOCTYPE html>
            <html>
              <head>
                <title>ITM University Exam System - GraphiQL</title>
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/graphiql/graphiql.min.css" />
              </head>
              <body style="margin: 0;">
                <div id="graphiql" style="height: 100vh;"></div>
                <script crossorigin src="https://cdn.jsdelivr.net/npm/react/umd/react.production.min.js"></script>
                <script crossorigin src="https://cdn.jsdelivr.net/npm/react-dom/umd/react-dom.production.min.js"></script>
                <script crossorigin src="https://cdn.jsdelivr.net/npm/graphiql/graphiql.min.js"></script>
                <script>
                  const fetcher = GraphiQL.createFetcher({{ url: '/graphql' }});
                  ReactDOM.render(
                    React.createElement(GraphiQL, {{ 
                        fetcher: fetcher,
                        defaultVariableEditorOpen: true,
                        headerEditorEnabled: true
                    }}),
                    document.getElementById('graphiql'),
                  );
                </script>
              </body>
            </html>
            '''
        
        data = request.get_json()
        result = schema.execute(
            data.get('query'),
            variable_values=data.get('variables'),
            context_value=request
        )
        
        response_data = {'data': result.data}
        if result.errors:
            response_data['errors'] = [str(err) for err in result.errors]
            
        return jsonify(response_data)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
