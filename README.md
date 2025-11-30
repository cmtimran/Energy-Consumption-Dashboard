# 🌍 World Energy Consumption Dashboard

## Overview
An interactive data visualization dashboard for analyzing global energy consumption patterns, trends, and correlations across multiple countries and time periods. Built with Python Dash and Plotly.

![Dashboard Type](https://img.shields.io/badge/Type-Interactive%20Dashboard-blue)
![Python](https://img.shields.io/badge/Python-3.x-green)
![Dash](https://img.shields.io/badge/Dash-Framework-red)
![Plotly](https://img.shields.io/badge/Plotly-Visualization-orange)

## 👨‍💻 Authors

**Imran Hossain** & **Nabid Osman**  
*University of Debrecen*  
*Data Visualization Lab - 1st Semester*

## 🌐 Live Demo

**🚀 [View Live Dashboard](https://energy-consumption-dashboard-n645.onrender.com/)**

Experience the interactive dashboard online! The application is hosted on Render and accessible worldwide.


## 📊 Project Description

This comprehensive dashboard provides in-depth analysis of global energy consumption patterns across multiple countries and time periods. The visualizations help identify:

- **Trends in fossil fuel usage** (Coal, Oil, Gas)
- **Renewable energy adoption** (Solar, Wind, Hydro, Biofuel)
- **Correlations between different energy sources**
- **Relationship between economic development (GDP) and energy consumption**
- **Greenhouse gas emissions patterns**

### Dataset Information
- **Source**: [World Energy Consumption (Kaggle)](https://www.kaggle.com/datasets/pralabhpoudel/world-energy-consumption)
- **Coverage**: 200+ Countries & Regions
- **Energy Sources**: Coal, Oil, Gas, Nuclear, Hydro, Solar, Wind, Biofuel, Other Renewables
- **Key Metrics**: Primary Energy (TWh), GDP (USD), GHG Emissions (Mt CO₂), Population
- **Time Range**: 1900–2020

## 🎯 Features

### Interactive Controls
1. **Country/Region Selection**: Choose from 200+ countries or view global aggregated data
2. **Year Range Slider**: Analyze trends within specific time periods
3. **Energy Source Checklist**: Filter visualizations by selecting specific energy sources

### 11 Visualizations

| # | Visualization | Description | Purpose |
|---|--------------|-------------|---------|
| 1 | **Pie Chart** | Energy Mix Distribution | Shows proportional share of selected energy sources |
| 2 | **Line Chart** | Total Primary Energy | Tracks overall energy consumption trends |
| 3 | **Multi-Line Chart** | Energy Source Trends | Compares consumption of different sources over time |
| 4 | **Stacked Area Chart** | Energy Composition | Displays absolute contribution of each source |
| 5 | **Stream Graph** | Proportional Mix | Shows relative share (%) of sources over time |
| 6 | **Sunburst Chart** | Hierarchical Energy Mix | Radial part-to-whole visualization |
| 7 | **Interactive Global Map (2D/3D)** | Global energy by country | Switch between 2D projections and 3D globe; supports per‑capita + animation |
| 8 | **Scatter Plot** | GDP vs Energy | Explores economic-energy relationship |
| 9 | **Bar Chart** | GHG Emissions | Annual greenhouse gas emissions trends |
| 10 | **Heatmap** | Source Correlation | Statistical correlations between sources |
| 11 | **Treemap** | Energy Breakdown | Rectangle-based hierarchical view |

## 🚀 Getting Started

### Prerequisites
- Python 3.x (3.7 or higher recommended)
- pip (Python package installer)
- Virtual environment (recommended)
- Minimum 4GB RAM
- Modern web browser (Chrome, Firefox, Edge, Safari)

### Required Libraries

The app directly uses only these Python packages (others are installed transitively):

- Dash — Web app framework ([docs](https://dash.plotly.com/))
- Plotly — Interactive charts ([docs](https://plotly.com/python/))
- Pandas — Data processing ([docs](https://pandas.pydata.org/))

### Installation

1. **Clone or download the project**
   ```bash
   cd ".\EnergyConsumptionDashboard"
   ```

2. **Create and activate virtual environment**
   
   **Windows:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
   
   **macOS/Linux:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install required packages**
   ```bash
   pip install --upgrade pip
   pip install dash==2.14.2
   pip install plotly==5.18.0
   pip install pandas==2.1.3
   ```
   
   **Or install from requirements.txt:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure dataset is in place**
   - File: `Data/World Energy Consumption.csv`
   - Verify file exists and is readable

### Running the Dashboard

```bash
python app.py
```

The dashboard will be available at: **http://127.0.0.1:8050/**

## 🌐 Deployment (Hosting Online)

This dashboard can be hosted online for free using **Render**. The project is already configured with the necessary deployment files.

### Deploy to Render (Recommended - Free)

1. **Sign up** at [render.com](https://render.com) (free account)

2. **Create a New Web Service**:
   - Click "New +" → "Web Service"
   - Connect your GitHub repository: `https://github.com/cmtimran/Energy-Consumption-Dashboard`
   - Render will auto-detect it's a Python app

3. **Configure the service**:
   - **Name**: `energy-dashboard` (or your choice)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:server`
   - **Instance Type**: `Free`

4. **Deploy**:
   - Click "Create Web Service"
   - Render will automatically build and deploy your app
   - You'll get a live URL like: `https://energy-dashboard.onrender.com`

### Alternative Hosting Options

- **Heroku**: Similar to Render, uses the same `Procfile` and `requirements.txt`
- **PythonAnywhere**: Good for Python apps, requires manual setup
- **Railway**: Modern platform with free tier

### Deployment Files Included

- `Procfile` - Tells the platform how to run the app
- `requirements.txt` - Lists all Python dependencies
- `app.py` - Already configured with `server = app.server` for deployment

**Note**: The free tier on Render may spin down after inactivity, so the first load might take 30-60 seconds.

## 🎨 Design & Styling

### Color Scheme
- **Primary Color**: #2C3E50 (Dark Blue-Gray)
- **Secondary Color**: #3498DB (Bright Blue)
- **Accent Color**: #E74C3C (Red)
- **Background**: #ECF0F1 (Light Gray)
- **Text**: #2C3E50 (Dark)

### Chart Template
- Uses `plotly_white` template for clean, professional appearance
- Consistent color schemes across all visualizations
- Responsive layout with two-column grid system
- Card-based design with shadows and rounded corners

## 📖 User Guide

### How to Use the Dashboard

1. **Select a Country**: Use the dropdown to choose a specific country or "World" for global data
2. **Choose Time Range**: Adjust the slider to focus on a specific period
3. **Filter Energy Sources**: Check/uncheck energy sources to customize visualizations
4. **Interact with Charts**:
   - Hover for detailed information
   - Click legend items to show/hide data
   - Zoom and pan on geographic maps
   - Rotate the 3D globe

### Understanding Each Visualization

#### 🥧 Energy Mix (Pie Chart)
- Shows percentage distribution of energy sources
- Best for: Understanding current energy composition
- Controlled by: Energy source checklist

#### 📉 Total Primary Energy (Line Chart)
- Displays overall energy consumption trend
- Best for: Identifying growth patterns
- Independent of energy source selection

#### 📊 Energy Source Trends (Multi-Line)
- Compares multiple sources simultaneously
- Best for: Comparing growth rates
- Controlled by: Energy source checklist

#### 📈 Stacked Area Chart
- Shows absolute contribution of each source
- Best for: Visualizing total volume changes
- Controlled by: Energy source checklist

#### 🌊 Stream Graph
- Displays relative share (100% stacked)
- Best for: Seeing portfolio shifts
- Controlled by: Energy source checklist

#### ☀️ Sunburst Chart
- Radial hierarchical breakdown
- Best for: Alternative part-to-whole view
- Controlled by: Energy source checklist

#### 🌍 Interactive Global Energy Map (2D/3D)
- Switch between multiple 2D projections and a 3D globe
- Options: Per‑capita normalization and animation by year
- Best for: Regional patterns and a global perspective in one chart

#### 💰 GDP vs Energy Scatter Plot
- Each point = one year
- Best for: Analyzing energy intensity of growth
- Includes: Trend line for correlation

#### 🏭 GHG Emissions Bar Chart
- Annual emissions over time
- Best for: Environmental impact assessment
- Independent visualization

#### 🔥 Correlation Heatmap
- Statistical relationships between sources
- Best for: Understanding interdependencies
- Requires: At least 2 energy sources selected

#### 🌳 Energy Treemap
- Rectangle sizes = consumption volumes
- Best for: Hierarchical comparison
- Controlled by: Energy source checklist

## 🛠️ Technical Details

### Project Structure
```
EnergyConsumptionDashboard/
│
├── app.py                          # Main application file (575+ lines)
├── Data/
│   └── World Energy Consumption.csv # Dataset (200+ countries, 100+ years)
├── .venv/                          # Virtual environment
├── README.md                       # This comprehensive documentation
└── requirements.txt                # Python dependencies (optional)
```

### Technology Stack

#### Core Framework: Dash (v2.14+)
**Purpose**: Building interactive web applications  
**Key Features Used**:
- `dash.Dash()`: Main application instance
- `dcc.Graph`: Plotly chart components
- `dcc.Dropdown`: Country selection widget
- `dcc.RangeSlider`: Year range selection
- `dcc.Checklist`: Energy source filter
- `dcc.Loading`: Loading state indicators
- `html.*`: HTML components (Div, H1, H2, H3, H4, P, Label)
- `Input/Output`: Callback decorators for interactivity

**Why Dash?**
- Purely Python-based (no JavaScript needed)
- Reactive programming model
- Built-in Flask server
- Production-ready

#### Visualization Library: Plotly Express (v5.18+)
**Purpose**: High-level charting interface  
**Chart Types Used**:
1. `px.pie()`: Pie charts
2. `px.line()`: Line charts
3. `px.area()`: Area and stacked area charts
4. `px.scatter()`: Scatter plots
5. `px.bar()`: Bar charts
6. `px.choropleth()`: Geographic maps
7. `px.scatter_geo()`: 3D globe visualization
8. `px.imshow()`: Heatmaps
9. `px.treemap()`: Treemap charts
10. `px.sunburst()`: Sunburst charts

**Advanced Features**:
- `groupnorm='fraction'`: Percentage stacking in stream graphs
- `color_discrete_sequence`: Custom color palettes
- `template`: Theme system (plotly_white)
- `trendline="ols"`: Regression lines in scatter plots
- `hover_data`: Custom tooltip information

#### Data Processing: Pandas (v2.0+)
**Purpose**: Data manipulation and analysis  
**Operations Used**:
- `pd.read_csv()`: CSV data loading
- `df.melt()`: Wide-to-long data transformation
- `df.corr()`: Correlation matrix calculation
- `df.fillna()`: Handling missing values
- Boolean indexing: Filtering data by country and year
- String operations: `.str.replace()`, `.str.capitalize()`, `.str.title()`

### Key Technologies

| Component | Technology | Version | License |
|-----------|-----------|---------|---------|
| Language | Python | 3.7+ | PSF |
| Framework | Dash | 2.14+ | MIT |
| Charting | Plotly | 5.18+ | MIT |
| Data | Pandas | 2.0+ | BSD |
| Server | Flask | 2.3+ | BSD |
| WSGI | Werkzeug | 2.3+ | BSD |

### Dependencies Graph
```
Your Application (app.py)
    │
    ├── Dash (Web Framework)
    │   ├── Flask (HTTP Server)
    │   │   └── Werkzeug (WSGI Utilities)
    │   ├── Plotly (Visualization)
    │   └── React (UI - bundled)
    │
    └── Pandas (Data Processing)
        └── NumPy (Numerical Computing)
```

### Code Organization & Architecture

```python
# File Structure (app.py):

# 1. IMPORTS (Lines 1-5)
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# 2. CONFIGURATION (Lines 7-58)
- Data Loading: pd.read_csv()
- Chart Template: CHART_TEMPLATE = 'plotly_white'
- Color Constants: PRIMARY_COLOR, SECONDARY_COLOR, etc.
- Style Dictionaries: CUSTOM_STYLE, HEADER_STYLE, etc.

# 3. APP INITIALIZATION (Lines 19-20)
app = dash.Dash(__name__)
app.title = "World Energy Consumption Dashboard"

# 4. LAYOUT DEFINITION (Lines 60-275)
app.layout = html.Div([
    - Header Section (Lines 62-70)
    - About Section (Lines 72-86)
    - Control Panel (Lines 88-145)
    - 12 Visualization Cards (Lines 147-269)
    - Footer (Lines 271-275)
])

# 5. CALLBACK FUNCTION (Lines 277-565)
@app.callback(
    [Output(...) × 12],  # 12 chart outputs
    [Input(...) × 3]      # 3 user inputs
)
def update_graphs(country, year_range, energy_sources):
    # Data filtering
    # Chart generation (12 different types)
    # Error handling for each chart
    # Return list of 12 figures

# 6. SERVER EXECUTION (Lines 567-570)
if __name__ == '__main__':
    app.run(debug=False)
```

### Data Flow Architecture

```
┌─────────────────────────────────────────────────────┐
│  USER INTERACTION                                    │
│  - Selects Country                                   │
│  - Adjusts Year Range                                │
│  - Checks/Unchecks Energy Sources                    │
└────────────────┬────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────┐
│  DASH CALLBACK TRIGGERED                             │
│  Function: update_graphs(country, years, sources)    │
└────────────────┬────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────┐
│  DATA FILTERING (Pandas)                             │
│  filtered_df = df[                                   │
│      (df['country'] == selected_country) &           │
│      (df['year'] >= year_range[0]) &                 │
│      (df['year'] <= year_range[1])                   │
│  ]                                                   │
└────────────────┬────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────┐
│  CHART GENERATION (Plotly Express)                   │
│  For each of 12 visualizations:                      │
│    1. Transform data (melt, corr, etc.)              │
│    2. Create figure (px.line, px.pie, etc.)          │
│    3. Apply styling (colors, template)               │
│    4. Handle errors (try/except)                     │
└────────────────┬────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────┐
│  RETURN TO DASH                                      │
│  return [fig1, fig2, ..., fig12]                     │
└────────────────┬────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────┐
│  BROWSER UPDATE                                      │
│  - All 12 graphs refresh simultaneously              │
│  - Loading indicators disappear                      │
│  - Charts become interactive                         │
└─────────────────────────────────────────────────────┘
```

### Detailed Library Usage

#### 1. Dash Components (`dash` library)

**Core Components:**
```python
from dash import dcc, html
from dash.dependencies import Input, Output

# Application Instance
app = dash.Dash(__name__)

# HTML Components (html.*)
html.Div()      # Container divs
html.H1-H4()    # Headings
html.P()        # Paragraphs
html.Label()    # Form labels
html.Strong()   # Bold text

# Dash Core Components (dcc.*)
dcc.Graph()         # Plotly chart container
dcc.Dropdown()      # Dropdown selector
dcc.RangeSlider()   # Two-handle slider
dcc.Checklist()     # Multiple checkboxes
dcc.Loading()       # Loading spinner wrapper

# Callback System
@app.callback(
    [Output('component-id', 'property')],  # What to update
    [Input('component-id', 'property')]     # What triggers update
)
def callback_function(input_value):
    # Process and return output
    return output_value
```

**Usage in This Project:**
- 12 `dcc.Graph` components for visualizations
- 1 `dcc.Dropdown` for country selection (200+ options)
- 1 `dcc.RangeSlider` for year range (custom marks every 10 years)
- 1 `dcc.Checklist` for energy sources (9 options)
- 12 `dcc.Loading` wrappers for user feedback
- 1 main callback function with 3 inputs and 12 outputs

#### 2. Plotly Express (`plotly.express`)

**Configuration:**
```python
import plotly.express as px

# Global settings
CHART_TEMPLATE = 'plotly_white'  # Light theme
```

**Chart Examples:**

**Pie Chart:**
```python
fig = px.pie(
    values=energy_values,
    names=energy_labels,
    title='Energy Mix',
    template=CHART_TEMPLATE,
    color_discrete_sequence=px.colors.qualitative.Bold
)
fig.update_traces(textposition='inside', textinfo='percent+label')
```

**Line Chart with Styling:**
```python
fig = px.line(
    filtered_df,
    x='year',
    y='primary_energy_consumption',
    title='Energy Consumption',
    template=CHART_TEMPLATE
)
fig.update_traces(line_color=SECONDARY_COLOR, line_width=3)
fig.update_layout(hovermode='x unified')
```

**Choropleth Map:**
```python
fig = px.choropleth(
    map_df,
    locations="iso_code",
    color="primary_energy_consumption",
    color_continuous_scale='YlOrRd',
    projection="natural earth",
    template=CHART_TEMPLATE
)
```

**Stream Graph (Stacked Area with Normalization):**
```python
fig = px.area(
    stream_df,
    x='year',
    y='Consumption',
    color='Energy Source',
    groupnorm='fraction',  # Key feature for percentage
    template=CHART_TEMPLATE
)
fig.update_layout(yaxis_tickformat='.0%')  # Show as percentage
```

#### 3. Pandas (`pandas` library)

**Data Loading:**
```python
import pandas as pd
df = pd.read_csv('Data/World Energy Consumption.csv')
```

**Data Transformations:**
```python
# Filtering
filtered_df = df[(df['country'] == 'World') & 
                 (df['year'] >= 2000) & 
                 (df['year'] <= 2020)]

# Reshaping (Wide to Long)
melted_df = filtered_df.melt(
    id_vars=['year'], 
    value_vars=['coal_consumption', 'oil_consumption'],
    var_name='Energy Source',
    value_name='Consumption'
)

# Correlation Matrix
correlation_df = filtered_df[energy_sources].corr()

# Handling Missing Data
df['column'].fillna(0)

# String Operations
df['Energy Source'].str.replace('_consumption', '')
df['Energy Source'].str.title()
```

### Performance Characteristics

| Metric | Value | Notes |
|--------|-------|-------|
| Initial Load Time | 2-3 seconds | Depends on dataset size |
| Callback Execution | < 1 second | For most country selections |
| Memory Usage | ~200-300 MB | With full dataset loaded |
| Dataset Size | ~50 MB | CSV file |
| Number of Records | ~20,000 rows | Varies by dataset |
| Concurrent Users | 1 (development) | Use WSGI server for production |
| Browser Compatibility | 95%+ | Modern browsers |

### Error Handling

**Try-Except Blocks:**
Every chart generation is wrapped in error handling:
```python
try:
    # Chart generation code
    fig = px.line(...)
except Exception as e:
    # Fallback error message
    fig = {'layout': {'title': f'Error: {str(e)}', 'template': CHART_TEMPLATE}}
```

**Common Errors Handled:**
- Empty dataframe after filtering
- Missing columns in dataset
- Invalid date ranges
- No energy sources selected
- Correlation with < 2 sources

### Code Organization
```python
# Main Components:
1. Configuration & Imports (Lines 1-58)
   - Library imports
   - Data loading
   - Global constants (colors, styles, template)
   - Style dictionaries

2. App Initialization (Lines 19-20)
   - Dash app instance
   - Page title configuration

3. Layout Definition (Lines 60-275)
   - Header with project info
   - About section
   - Interactive control panel
   - 12 visualization cards (2×6 grid)
   - Footer

4. Callback Function (Lines 277-565)
   - Input handling (3 inputs)
   - Data filtering logic
   - 12 chart generators with error handling
   - Output return (12 figures)

5. App Execution (Lines 567-570)
   - Development server startup
```

### Library API Reference

#### Dash API Used

**Application Setup:**
```python
dash.Dash(__name__)              # Create app instance
app.title = "Title"              # Set browser tab title
app.layout = html.Div([...])     # Define UI structure
app.run(debug=False)             # Start server
```

**Callbacks:**
```python
@app.callback(
    [Output('id', 'figure'), ...],  # Multiple outputs
    [Input('id', 'value'), ...]      # Multiple inputs
)
```

**HTML Components:**
```python
html.Div(children=[], style={})     # Container
html.H1("Text", style={})           # Heading level 1
html.H2-H4("Text", style={})        # Other headings
html.P(["Text", html.Strong(...)])  # Paragraph
html.Label("Text", style={})        # Form label
```

**Core Components:**
```python
dcc.Graph(id='chart-id', figure=fig)
dcc.Dropdown(
    id='dropdown-id',
    options=[{'label': 'A', 'value': 'a'}],
    value='default',
    clearable=False
)
dcc.RangeSlider(
    id='slider-id',
    min=0,
    max=100,
    value=[25, 75],
    marks={0: '0', 100: '100'},
    tooltip={"placement": "bottom"}
)
dcc.Checklist(
    id='check-id',
    options=[{'label': 'A', 'value': 'a'}],
    value=['a'],
    labelStyle={'display': 'inline-block'}
)
dcc.Loading(children=[dcc.Graph(...)])
```

#### Plotly Express API Used

**Chart Creation Functions:**
```python
px.pie(values, names, title, template, color_discrete_sequence)
px.line(df, x, y, title, labels, template, color)
px.area(df, x, y, color, groupnorm, template)
px.scatter(df, x, y, hover_name, title, trendline, template)
px.bar(df, x, y, title, labels, template)
px.choropleth(df, locations, color, hover_name, projection, template)
px.scatter_geo(df, locations, size, color, projection, template)
px.imshow(array, labels, x, y, title, color_continuous_scale, template)
px.treemap(df, path, values, title, color, template)
px.sunburst(df, path, values, title, template)
```

**Figure Customization:**
```python
fig.update_traces(
    line_color='#color',
    line_width=3,
    marker=dict(size=10, color='#color'),
    textposition='inside',
    textinfo='percent+label'
)

fig.update_layout(
    hovermode='x unified',
    legend=dict(orientation='h', y=1.02),
    yaxis_tickformat='.0%',
    geo=dict(showframe=False)
)
```

**Color Schemes:**
```python
px.colors.qualitative.Bold      # Categorical colors
px.colors.sequential.YlOrRd     # Yellow-Orange-Red
px.colors.sequential.Plasma     # Purple-Pink-Yellow
'RdBu_r'                        # Red-Blue reversed
```

#### Pandas API Used

**Data Loading:**
```python
pd.read_csv('file.csv')
```

**Data Selection:**
```python
df['column']                    # Select column
df[['col1', 'col2']]           # Select multiple columns
df[df['col'] == value]         # Boolean filtering
df[(condition1) & (condition2)] # Multiple conditions
```

**Data Transformation:**
```python
df.melt(
    id_vars=['id_col'],
    value_vars=['val1', 'val2'],
    var_name='category',
    value_name='value'
)
df.corr()                       # Correlation matrix
df.fillna(value)                # Fill missing values
df.reset_index()                # Reset index
```

**String Operations:**
```python
df['col'].str.replace('old', 'new')
df['col'].str.capitalize()
df['col'].str.title()
df['col'].str.upper()
```

**Aggregation:**
```python
df['year'].min()                # Minimum value
df['year'].max()                # Maximum value
df['year'].unique()             # Unique values
df.iloc[0]                      # First row
df.empty                        # Check if empty
```

### Environment Setup Details

**Virtual Environment:**
```bash
# Why use virtual environment?
- Isolates project dependencies
- Prevents version conflicts
- Makes deployment reproducible
- Keeps global Python clean

# Commands:
python -m venv .venv            # Create
.venv\Scripts\activate          # Activate (Windows)
source .venv/bin/activate       # Activate (macOS/Linux)
deactivate                      # Deactivate
```

**Dependencies Installation:**
```bash
# Individual packages
pip install dash==2.14.2
pip install plotly==5.18.0
pip install pandas==2.1.3

# From requirements file
pip install -r requirements.txt

# Upgrade pip first (recommended)
pip install --upgrade pip

# Check installed versions
pip list
pip show dash
```

### System Requirements

**Hardware:**
- Processor: Intel i3 or equivalent (2.0 GHz+)
- RAM: 4 GB minimum, 8 GB recommended
- Disk Space: 500 MB for environment and dependencies
- Network: Required for initial package installation

**Software:**
- Operating System: Windows 10/11, macOS 10.14+, Ubuntu 18.04+
- Python: 3.7, 3.8, 3.9, 3.10, 3.11 (3.10+ recommended)
- Browser: Chrome 90+, Firefox 88+, Edge 90+, Safari 14+
- Terminal: PowerShell (Windows), Terminal (macOS/Linux)

### Configuration Files

**requirements.txt (Create this file):**
```txt
dash==2.14.2
plotly==5.18.0
pandas==2.1.3
Flask==2.3.3
Werkzeug==2.3.7
```

**Usage:**
```bash
pip install -r requirements.txt
```

**Generate requirements.txt:**
```bash
pip freeze > requirements.txt
```

## 📊 Data Flow

```
User Interaction → Controls (Dropdown/Slider/Checklist)
       ↓
Dash Callback Triggered
       ↓
Data Filtering (by country & year range)
       ↓
Generate 12 Figures (using selected sources)
       ↓
Update Dashboard Display
```

## 🔍 Key Insights You Can Discover

1. **Energy Transition**: Track the shift from fossil fuels to renewables
2. **Economic Correlation**: Understand GDP-energy relationships
3. **Regional Patterns**: Identify high-consumption regions
4. **Source Dependencies**: See which sources are correlated
5. **Emissions Trends**: Monitor environmental impact
6. **Portfolio Changes**: Visualize energy mix evolution

## 🎓 Educational Value

This dashboard is ideal for:
- **Students**: Learning data visualization techniques
- **Researchers**: Analyzing energy consumption patterns
- **Policy Makers**: Understanding global energy trends
- **Educators**: Teaching energy economics and sustainability
- **Analysts**: Exploring correlations and relationships

## 📈 Performance Notes

- Dashboard loads all data into memory (efficient for this dataset size)
- Callbacks execute in real-time (< 1 second for most selections)
- All 12 visualizations update simultaneously
- Responsive design works on various screen sizes

## 🔧 Customization

### Adding New Energy Sources
1. Ensure column exists in CSV with `_consumption` suffix
2. Add to checklist options in layout
3. No additional code changes needed!

### Modifying Colors
Edit these constants at the top of `app.py`:
```python
PRIMARY_COLOR = '#2C3E50'
SECONDARY_COLOR = '#3498DB'
ACCENT_COLOR = '#E74C3C'
```

### Adding New Countries
Simply ensure the country exists in the dataset CSV file.

## ⚠️ Known Limitations

1. **Debug Mode**: Currently disabled (`debug=False`) due to environment compatibility
2. **Data Gaps**: Some countries may have incomplete historical data
3. **Memory**: Large time ranges for world data may be memory-intensive

## 🆘 Troubleshooting

### Dashboard won't start
- Ensure Python 3.x is installed
- Verify all dependencies: `pip list`
- Check if port 8050 is available

### Charts not updating
- Ensure at least one energy source is selected (for filtered charts)
- Check browser console for JavaScript errors
- Try refreshing the browser

### Missing data warnings
- Some countries have limited historical data
- Select a broader time range or different country

## 📝 Future Enhancements

Potential improvements:
- [ ] Add data export functionality (CSV/Excel)
- [ ] Implement chart download (PNG/SVG)
- [ ] Add year-over-year comparison mode
- [ ] Include forecasting/predictions
- [ ] Add continent-level aggregation
- [ ] Implement custom date range picker
- [ ] Add more statistical analysis tools

## 👨‍💻 Development

### Contributing
Feel free to fork, modify, and submit pull requests!

### Testing Locally
```bash
# Run the app
python app.py

# Access at http://127.0.0.1:8050/
```

## 📄 License

This project is created for educational purposes as part of the Data Visualization Lab coursework at the University of Debrecen.

## 🙏 Acknowledgments

- **Dataset**: World Energy Consumption data providers
- **Framework**: Plotly Dash development team
- **Institution**: University of Debrecen
- **Course**: Data Visualization Lab (1st Semester)

## 📞 Support

For questions or issues:
1. Check this README first
2. Review the code comments in `app.py`
3. Consult Dash documentation: https://dash.plotly.com/
4. Contact course instructors

## 📚 Library Documentation & Resources

### Official Documentation

#### Dash Framework
- **Official Site**: https://dash.plotly.com/
- **Tutorial**: https://dash.plotly.com/tutorial
- **Component Gallery**: https://dash.plotly.com/dash-core-components
- **Callback Guide**: https://dash.plotly.com/basic-callbacks
- **Layout Guide**: https://dash.plotly.com/layout
- **GitHub**: https://github.com/plotly/dash
- **Community Forum**: https://community.plotly.com/c/dash/

**Key Topics for This Project:**
- [Getting Started](https://dash.plotly.com/installation)
- [Interactive Visualizations](https://dash.plotly.com/interactive-graphing)
- [Dash Core Components](https://dash.plotly.com/dash-core-components)
- [Dash HTML Components](https://dash.plotly.com/dash-html-components)
- [Callbacks with Multiple Inputs/Outputs](https://dash.plotly.com/basic-callbacks#dash-app-with-multiple-outputs)
- [Loading States](https://dash.plotly.com/loading-states)

#### Plotly Python
- **Official Site**: https://plotly.com/python/
- **Express API**: https://plotly.com/python/plotly-express/
- **Chart Types**: https://plotly.com/python/chart-types/
- **Styling**: https://plotly.com/python/templates/
- **GitHub**: https://github.com/plotly/plotly.py
- **Reference**: https://plotly.com/python-api-reference/

**Charts Used in This Project:**
- [Pie Charts](https://plotly.com/python/pie-charts/)
- [Line Charts](https://plotly.com/python/line-charts/)
- [Area Charts](https://plotly.com/python/filled-area-plots/)
- [Scatter Plots](https://plotly.com/python/line-and-scatter/)
- [Bar Charts](https://plotly.com/python/bar-charts/)
- [Choropleth Maps](https://plotly.com/python/choropleth-maps/)
- [Scatter Geo Maps](https://plotly.com/python/scatter-plots-on-maps/)
- [Heatmaps](https://plotly.com/python/heatmaps/)
- [Treemaps](https://plotly.com/python/treemaps/)
- [Sunburst Charts](https://plotly.com/python/sunburst-charts/)

#### Pandas
- **Official Site**: https://pandas.pydata.org/
- **Getting Started**: https://pandas.pydata.org/getting_started.html
- **User Guide**: https://pandas.pydata.org/docs/user_guide/index.html
- **API Reference**: https://pandas.pydata.org/docs/reference/index.html
- **10 Minutes to Pandas**: https://pandas.pydata.org/docs/user_guide/10min.html
- **GitHub**: https://github.com/pandas-dev/pandas

**Operations Used in This Project:**
- [Reading CSV Files](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)
- [Boolean Indexing](https://pandas.pydata.org/docs/user_guide/indexing.html#boolean-indexing)
- [Reshaping with melt()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.melt.html)
- [Correlation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html)
- [Handling Missing Data](https://pandas.pydata.org/docs/user_guide/missing_data.html)
- [String Methods](https://pandas.pydata.org/docs/user_guide/text.html)

### Video Tutorials

**Dash Framework:**
- [Plotly Dash Tutorial - YouTube](https://www.youtube.com/results?search_query=plotly+dash+tutorial)
- [Building Web Apps with Dash](https://www.youtube.com/watch?v=hSPmj7mK6ng)
- [Dash in 20 Minutes](https://www.youtube.com/watch?v=dgV3GGFMcTc)

**Plotly Charts:**
- [Plotly Python Tutorial](https://www.youtube.com/results?search_query=plotly+python+tutorial)
- [Data Visualization with Plotly](https://www.youtube.com/watch?v=GGL6U0k8WYA)

**Pandas:**
- [Pandas Tutorial](https://www.youtube.com/results?search_query=pandas+tutorial)
- [Data Analysis with Pandas](https://www.youtube.com/watch?v=vmEHCJofslg)

### Books & Learning Resources

**Recommended Books:**
1. **"Interactive Dashboards and Data Apps with Plotly and Dash"** by Elias Dabbas
2. **"Python for Data Analysis"** by Wes McKinney (Pandas creator)
3. **"Data Visualization with Python and JavaScript"** by Kyran Dale

**Online Courses:**
- [Plotly Dash Course on Udemy](https://www.udemy.com/topic/plotly-dash/)
- [DataCamp: Building Dashboards with Dash and Plotly](https://www.datacamp.com/)
- [Coursera: Data Visualization with Python](https://www.coursera.org/)

### Community & Support

**Stack Overflow Tags:**
- [plotly-dash](https://stackoverflow.com/questions/tagged/plotly-dash)
- [plotly-python](https://stackoverflow.com/questions/tagged/plotly-python)
- [pandas](https://stackoverflow.com/questions/tagged/pandas)

**Reddit Communities:**
- [r/datascience](https://www.reddit.com/r/datascience/)
- [r/Python](https://www.reddit.com/r/Python/)
- [r/learnpython](https://www.reddit.com/r/learnpython/)

**Discord/Slack:**
- [Plotly Community](https://community.plotly.com/)
- [Python Discord](https://discord.gg/python)

### Code Examples & Galleries

**Dash App Gallery:**
- https://dash.gallery/Portal/
- https://github.com/plotly/dash-sample-apps

**Plotly Examples:**
- https://plotly.com/python/
- https://github.com/plotly/plotly.py/tree/master/doc/python

### Troubleshooting Resources

**Common Issues & Solutions:**
- [Dash Troubleshooting Guide](https://dash.plotly.com/troubleshooting)
- [Plotly FAQ](https://plotly.com/python/getting-started/#frequently-asked-questions)
- [Pandas FAQ](https://pandas.pydata.org/docs/user_guide/gotchas.html)

### Version Compatibility

| Python | Dash | Plotly | Pandas | Status |
|--------|------|--------|--------|--------|
| 3.7 | 2.14+ | 5.18+ | 2.0+ | ✅ Supported |
| 3.8 | 2.14+ | 5.18+ | 2.0+ | ✅ Supported |
| 3.9 | 2.14+ | 5.18+ | 2.0+ | ✅ Supported |
| 3.10 | 2.14+ | 5.18+ | 2.0+ | ✅ Recommended |
| 3.11 | 2.14+ | 5.18+ | 2.0+ | ✅ Supported |
| 3.12 | 2.14+ | 5.18+ | 2.1+ | ✅ Supported |

### License Information

All libraries used are open-source:

| Library | License | Commercial Use |
|---------|---------|----------------|
| Dash | MIT | ✅ Yes |
| Plotly | MIT | ✅ Yes |
| Pandas | BSD 3-Clause | ✅ Yes |
| Flask | BSD 3-Clause | ✅ Yes |
| Werkzeug | BSD 3-Clause | ✅ Yes |

**This means:**
- Free to use for any purpose
- Can modify and distribute
- Commercial use allowed
- No warranty provided

### Citation

If you use this project in academic work, please cite:

```bibtex
@software{energy_dashboard_2025_hossain,
  title = {World Energy Consumption Dashboard},
  author = {Hossain, Imran},
  year = {2025},
  institution = {University of Debrecen},
  course = {Data Visualization Lab},
  url = {https://github.com/cmtimran/Energy-Consumption-Dashboard}
}

@software{energy_dashboard_2025_osman,
  title = {World Energy Consumption Dashboard},
  author = {Osman, Nabid},
  year = {2025},
  institution = {University of Debrecen},
  course = {Data Visualization Lab},
  url = {https://github.com/Nabid08}
}
```

**Libraries to cite:**
```bibtex
@article{plotly,
  title = {Plotly Technologies Inc.},
  author = {Plotly},
  year = {2015},
  url = {https://plotly.com}
}

@software{pandas,
  title = {pandas-dev/pandas: Pandas},
  author = {The pandas development team},
  year = {2020},
  publisher = {Zenodo},
  doi = {10.5281/zenodo.3509134},
  url = {https://doi.org/10.5281/zenodo.3509134}
}
```

---

**Built with ❤️ using Dash & Plotly**

*Last Updated: November 2025*
*Version: 1.0.0*
