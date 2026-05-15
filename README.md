# AI Research Agent

A comprehensive AI-powered research agent system that integrates graph-based processing, document generation, and interactive web interfaces.

## Project Structure

- **app.py** - Main application entry point
- **streamlit_app.py** - Interactive web interface built with Streamlit
- **graph.py** - Graph data structure and processing logic
- **nodes.py** - Node definitions for graph construction
- **tools.py** - Utility functions and tools
- **pdf_generator.py** - PDF document generation capabilities
- **requirement.txt** - Python dependencies

## Features

- Graph-based data processing and analysis
- PDF document generation from research outputs
- Interactive web interface with Streamlit
- Modular tool-based architecture

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd AI Research Agent
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirement.txt
```

## Usage

### Running the Streamlit Web App
```bash
streamlit run streamlit_app.py
```

### Running the Main Application
```bash
python app.py
```

## Deployment

The application is deployed and accessible at:
[https://ai-research-agent-1-8yvr.onrender.com/](https://ai-research-agent-1-8yvr.onrender.com/)

## Dependencies

See `requirement.txt` for all required packages.

## Configuration

Set up any necessary environment variables in a `.env` file (excluded via .gitignore).

## Development

- Use `venv` for isolated Python environments
- Install development dependencies as needed


## License

[Add license information here]

## Author

[Add author information here]
