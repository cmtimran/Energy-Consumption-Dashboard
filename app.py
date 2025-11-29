import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Data load
df = pd.read_csv('Data/World Energy Consumption.csv')

# Color palette
CHART_TEMPLATE = 'plotly_white'
PRIMARY_COLOR = '#2C3E50'
SECONDARY_COLOR = '#3498DB'
ACCENT_COLOR = '#E74C3C'
BACKGROUND_COLOR = '#ECF0F1'
TEXT_COLOR = '#2C3E50'

# Initialize application
app = dash.Dash(
    __name__,
    external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"]
)
app.title = "World Energy Consumption Dashboard"
server = app.server  # Expose the Flask server for deployment

# Define custom style
CUSTOM_STYLE = {
    'fontFamily': "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
    'backgroundColor': BACKGROUND_COLOR,
    'color': TEXT_COLOR,
    'padding': '0',
    'margin': '0'
}

HEADER_STYLE = {
    'backgroundColor': PRIMARY_COLOR,
    'color': 'white',
    'padding': '30px 20px',
    'marginBottom': '0',
    'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'
}

CONTROL_PANEL_STYLE = {
    'backgroundColor': 'white',
    'padding': '25px',
    'marginBottom': '20px',
    'borderRadius': '8px',
    'boxShadow': '0 2px 8px rgba(0,0,0,0.1)'
}

SECTION_STYLE = {
    'marginBottom': '15px'
}

LABEL_STYLE = {
    'fontWeight': '600',
    'color': PRIMARY_COLOR,
    'marginBottom': '8px',
    'fontSize': '14px',
    'display': 'block'
}

# Dashboard layout
app.layout = html.Div(style=CUSTOM_STYLE, children=[
    
    # Header
    html.Div(style=HEADER_STYLE, children=[
        html.Div(style={'maxWidth': '1200px', 'margin': '0 auto'}, children=[
            html.H1("🌍 World Energy Consumption Dashboard", 
                   style={'margin': '0 0 10px 0', 'fontSize': '36px', 'fontWeight': '700'}),
            html.P("An Interactive Data Visualization Platform for Analyzing Global Energy Trends and Consumption Patterns",
                  style={'margin': '0', 'fontSize': '16px', 'opacity': '0.9'}),
        ])
    ]),

    # Project overview
    html.Div(style={'maxWidth': '1200px', 'margin': '20px auto', 'padding': '0 20px'}, children=[
        html.Div(style={**CONTROL_PANEL_STYLE, 'marginBottom': '25px'}, children=[
            html.H3("📊 Overview", style={'color': PRIMARY_COLOR, 'marginTop': '0', 'marginBottom': '15px'}),
            html.P([
                "This interactive dashboard visualizes global energy consumption patterns from 1900 to 2020, covering over 200 countries and regions. ",
                "Analyze how energy sources have evolved from fossil fuel dominance to emerging renewable adoption, explore correlations between ",
                "economic growth (GDP) and energy demand, and track environmental impacts through greenhouse gas emissions data. ",
                "The platform combines 11 different visualization types to provide comprehensive insights into the global energy transition."
            ], style={'lineHeight': '1.6', 'marginBottom': '10px'}),
            html.P([
                html.Strong("Dataset: "), 
                html.A("World Energy Consumption (1900-2020)", 
                       href="https://www.kaggle.com/datasets/pralabhpoudel/world-energy-consumption", 
                       target="_blank",
                       style={'color': PRIMARY_COLOR, 'textDecoration': 'none', 'fontWeight': 'bold'}),
                " | ",
                html.Strong("Coverage: "), "200+ Countries & Regions | ",
                html.Strong("Sources: "), "Coal, Oil, Gas, Nuclear, Hydro, Solar, Wind, Biofuel, Other Renewables | ",
                html.Strong("Key Metrics: "), "Primary Energy (TWh), GDP (USD), GHG Emissions (Mt CO₂), Population"
            ], style={'lineHeight': '1.6', 'fontSize': '14px', 'color': '#555'}),
        ]),

        # control panel: Country, year range, and energy source filters
        html.Div(style=CONTROL_PANEL_STYLE, children=[
            html.H3("⚙️ Controls", style={'color': PRIMARY_COLOR, 'marginTop': '0', 'marginBottom': '20px'}),
            
            # Country/Region selector
            html.Div(style=SECTION_STYLE, children=[
                html.Label("Select Country / Region:", style=LABEL_STYLE),
                dcc.Dropdown(
                    id='country-dropdown',
                    options=[{'label': str(country).title(), 'value': country} for country in df['country'].unique()],
                    value='World',
                    style={'marginBottom': '10px'},
                    clearable=False
                ),
                html.P("Choose a specific country or 'World' for global aggregated data.", 
                      style={'fontSize': '12px', 'color': '#777', 'marginTop': '5px', 'fontStyle': 'italic'})
            ]),

            # Time period selector
            html.Div(style=SECTION_STYLE, children=[
                html.Label("Select Year Range:", style=LABEL_STYLE),
                dcc.RangeSlider(
                    id='year-slider',
                    min=df['year'].min(),
                    max=df['year'].max(),
                    value=[df['year'].min(), df['year'].max()],
                    marks={str(year): {'label': str(year), 'style': {'fontSize': '11px'}} 
                           for year in df['year'].unique() if year % 10 == 0},
                    tooltip={"placement": "bottom", "always_visible": False}
                ),
                html.P("Adjust the slider to analyze trends within a specific time period.", 
                      style={'fontSize': '12px', 'color': '#777', 'marginTop': '15px', 'fontStyle': 'italic'})
            ]),

            # Energy source selector
            html.Div(style=SECTION_STYLE, children=[
                html.Label("Select Energy Sources to Analyze:", style=LABEL_STYLE),
                dcc.Checklist(
                    id='energy-source-checklist',
                    options=[{'label': ' ' + source.replace('_consumption', '').replace('_', ' ').title(), 'value': source} 
                            for source in ['coal_consumption', 'oil_consumption', 'gas_consumption', 'nuclear_consumption', 
                                          'hydro_consumption', 'solar_consumption', 'wind_consumption', 
                                          'biofuel_consumption', 'other_renewable_consumption']],
                    value=['coal_consumption', 'oil_consumption', 'gas_consumption'],
                    labelStyle={'display': 'inline-block', 'marginRight': '15px', 'marginBottom': '8px'},
                    style={'marginTop': '10px'}
                ),
                html.P("These selections will filter data in the Pie Chart, Trend Chart, Heatmap, Stacked Area, Stream Graph, Sunburst, and Treemap.", 
                      style={'fontSize': '12px', 'color': '#777', 'marginTop': '10px', 'fontStyle': 'italic'})
            ]),
        ])        
    ]),

    # Visualization charts and graphs
    html.Div(style={'maxWidth': '1200px', 'margin': '0 auto', 'padding': '0 20px'}, children=[
        
        # First row: Energy Mix (Pie Chart) and Total Primary Energy Consumption (Line Chart)
        html.Div([
            html.Div([
                html.Div(style={ 'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '8px', 'boxShadow': '0 2px 8px rgba(0,0,0,0.1)', 'height': '100%'}, children=[
                    html.H4("🥧 Energy Mix (Pie Chart)", style={'color': SECONDARY_COLOR, 'marginTop': '0'}),
                    html.P("Displays the proportional distribution of selected energy sources for the latest year in the chosen range. Use this to understand which sources dominate the energy mix.", 
                          style={'fontSize': '13px', 'color': '#666', 'marginBottom': '15px'}),
                    dcc.Loading(dcc.Graph(id='energy-mix-pie-chart'))
                ])
            ], className="six columns"),
            html.Div([
                html.Div(style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '8px', 'boxShadow': '0 2px 8px rgba(0,0,0,0.1)', 'height': '100%'}, children=[
                    html.H4("📉 Total Primary Energy Consumption (Line Chart)", style={'color': SECONDARY_COLOR, 'marginTop': '0'}),
                    html.P("Shows the overall trend of total primary energy consumption over the selected time period. Increasing trends indicate growing energy demand.", 
                          style={'fontSize': '13px', 'color': '#666', 'marginBottom': '15px'}),
                    dcc.Loading(dcc.Graph(id='primary-energy-consumption-line-chart'))
                ])
            ], className="six columns"),
        ], className="row", style={'marginBottom': '20px'}),

        # Row 2: Energy Source Trend Chart & Stacked Area Chart
        html.Div([
            html.Div([
                html.Div(style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '8px', 'boxShadow': '0 2px 8px rgba(0,0,0,0.1)', 'height': '100%'}, children=[
                    html.H4("📊 Energy Source Trends (Multi-Line Chart)", style={'color': SECONDARY_COLOR, 'marginTop': '0'}),
                    html.P("Compares the absolute consumption trends of selected energy sources over time. Each line represents a different source, allowing for direct comparison of growth rates.", 
                          style={'fontSize': '13px', 'color': '#666', 'marginBottom': '15px'}),
                    dcc.Loading(dcc.Graph(id='energy-source-trend-chart'))
                ])
            ], className="six columns"),
            html.Div([
                html.Div(style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '8px', 'boxShadow': '0 2px 8px rgba(0,0,0,0.1)', 'height': '100%'}, children=[
                    html.H4("📈 Stacked Energy Composition (Area Chart)", style={'color': SECONDARY_COLOR, 'marginTop': '0'}),
                    html.P("Illustrates the absolute contribution of each selected energy source to total consumption over time. The total height shows combined consumption, while each color represents a source.", 
                          style={'fontSize': '13px', 'color': '#666', 'marginBottom': '15px'}),
                    dcc.Loading(dcc.Graph(id='stacked-area-chart'))
                ])
            ], className="six columns"),
        ], className="row", style={'marginBottom': '20px'}),

        # Row 3: Stream Graph & Sunburst Chart
        html.Div([
            html.Div([
                html.Div(style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '8px', 'boxShadow': '0 2px 8px rgba(0,0,0,0.1)', 'height': '100%'}, children=[
                    html.H4("🌊 Proportional Energy Mix Over Time (Stream Graph)", style={'color': SECONDARY_COLOR, 'marginTop': '0'}),
                    html.P("Shows the relative share (percentage) of each selected energy source over time. All sources sum to 100%, revealing shifts in the energy portfolio composition.", 
                          style={'fontSize': '13px', 'color': '#666', 'marginBottom': '15px'}),
                    dcc.Loading(dcc.Graph(id='stream-graph'))
                ])
            ], className="six columns"),
            html.Div([
                html.Div(style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '8px', 'boxShadow': '0 2px 8px rgba(0,0,0,0.1)', 'height': '100%'}, children=[
                    html.H4("☀️ Energy Mix Hierarchy (Sunburst Chart)", style={'color': SECONDARY_COLOR, 'marginTop': '0'}),
                    html.P("A radial representation of the energy mix for the latest year. The interactive circular design provides an alternative part-to-whole view of selected sources.", 
                          style={'fontSize': '13px', 'color': '#666', 'marginBottom': '15px'}),
                    dcc.Loading(dcc.Graph(id='sunburst-chart'))
                ])
            ], className="six columns"),
        ], className="row", style={'marginBottom': '20px'}),

        # Row 4: Map
        html.Div([
            html.Div([
                html.Div(style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '8px', 'boxShadow': '0 2px 8px rgba(0,0,0,0.1)', 'height': '100%'}, children=[
                    html.H4("🌍 Interactive Global Energy Map", style={'color': SECONDARY_COLOR, 'marginTop': '0'}),
                    html.P("Geographic visualization of global primary energy consumption. Switch between different map projections to explore consumption patterns across countries.", 
                          style={'fontSize': '13px', 'color': '#666', 'marginBottom': '15px'}),
                    
                    # All controls
                    html.Div(style={'display': 'grid', 'gridTemplateColumns': '2fr 1.8fr 0.7fr 0.9fr', 'gap': '12px', 'alignItems': 'end', 'marginBottom': '15px'}, children=[
                        html.Div(children=[
                            html.Label("Select Energy Metric:", style={'fontWeight': '600', 'color': PRIMARY_COLOR, 'marginBottom': '8px', 'fontSize': '13px', 'display': 'block'}),
                            dcc.Dropdown(
                                id='map-metric-dropdown',
                                options=[
                                    {'label': '⚡ Total Primary Energy', 'value': 'primary_energy_consumption'},
                                    {'label': '⛏️ Coal Consumption', 'value': 'coal_consumption'},
                                    {'label': '🛢️ Oil Consumption', 'value': 'oil_consumption'},
                                    {'label': '🔥 Gas Consumption', 'value': 'gas_consumption'},
                                    {'label': '☢️ Nuclear Energy', 'value': 'nuclear_consumption'},
                                    {'label': '💧 Hydro Power', 'value': 'hydro_consumption'},
                                    {'label': '☀️ Solar Energy', 'value': 'solar_consumption'},
                                    {'label': '💨 Wind Energy', 'value': 'wind_consumption'},
                                    {'label': '🌱 Renewables (Total)', 'value': 'renewables_consumption'}
                                ],
                                value='primary_energy_consumption',
                                clearable=False
                            )
                        ]),
                        html.Div(children=[
                            html.Label("Select Map Projection:", style={'fontWeight': '600', 'color': PRIMARY_COLOR, 'marginBottom': '8px', 'fontSize': '13px', 'display': 'block'}),
                            dcc.Dropdown(
                                id='map-projection-dropdown',
                                options=[
                                    {'label': '🗺️  2D Natural Earth', 'value': 'natural earth'},
                                    {'label': '🌐  3D Globe', 'value': 'orthographic'},
                                    {'label': '📐  2D Equirectangular', 'value': 'equirectangular'},
                                    {'label': '🌍  2D Robinson', 'value': 'robinson'},
                                    {'label': '🧭  2D Mercator', 'value': 'mercator'}
                                ],
                                value='natural earth',
                                clearable=False,
                                style={'fontSize': '13px'}
                            )
                        ]),
                        html.Div(children=[
                            html.Label("Normalize:", style={'fontWeight': '600', 'color': PRIMARY_COLOR, 'marginBottom': '8px', 'fontSize': '13px', 'display': 'block'}),
                            dcc.Checklist(
                                id='map-percapita-toggle',
                                options=[{'label': ' Per Capita', 'value': 'per_capita'}],
                                value=[],
                                inputStyle={'marginRight': '6px'},
                                style={'fontSize': '13px'}
                            )
                        ]),
                        html.Div(children=[
                            html.Label("Animation:", style={'fontWeight': '600', 'color': PRIMARY_COLOR, 'marginBottom': '8px', 'fontSize': '13px', 'display': 'block'}),
                            dcc.Checklist(
                                id='map-animate-toggle',
                                options=[{'label': ' Enable', 'value': 'animate'}],
                                value=[],
                                inputStyle={'marginRight': '6px'},
                                style={'fontSize': '13px'}
                            )
                        ])
                    ]),
                    
                    # Year slider
                    html.Div(style={'marginBottom': '15px'}, children=[
                        html.Label("Select Year:", style={'fontWeight': '600', 'color': PRIMARY_COLOR, 'marginBottom': '8px', 'fontSize': '13px', 'display': 'block'}),
                        dcc.Slider(
                            id='map-year-slider',
                            min=int(df['year'].min()),
                            max=int(df['year'].max()),
                            value=int(df['year'].max()),
                            marks={int(y): {'label': str(int(y))} for y in sorted(df['year'].unique()) if int(y) % 10 == 0},
                            tooltip={'placement': 'bottom', 'always_visible': False}
                        )
                    ]),
                    
                    dcc.Loading(dcc.Graph(id='global-energy-map'))
                ])
            ], style={'width': '100%'}),
        ], className="row", style={'marginBottom': '20px'}),

        # Row 5: GDP vs Energy Scatter & GHG Emissions Bar Chart
        html.Div([
            html.Div([
                html.Div(style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '8px', 'boxShadow': '0 2px 8px rgba(0,0,0,0.1)', 'height': '100%'}, children=[
                    html.H4("💰 GDP vs. Energy Consumption (Scatter Plot)", style={'color': SECONDARY_COLOR, 'marginTop': '0'}),
                    html.P("Explores the relationship between economic output (GDP) and primary energy consumption. Each point represents a year, revealing the energy intensity of economic growth.", 
                          style={'fontSize': '13px', 'color': '#666', 'marginBottom': '15px'}),
                    dcc.Loading(dcc.Graph(id='gdp-vs-energy-scatter'))
                ])
            ], className="six columns"),
            html.Div([
                html.Div(style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '8px', 'boxShadow': '0 2px 8px rgba(0,0,0,0.1)', 'height': '100%'}, children=[
                    html.H4("🏭 Greenhouse Gas Emissions (Bar Chart)", style={'color': SECONDARY_COLOR, 'marginTop': '0'}),
                    html.P("Displays annual greenhouse gas emissions trends. Rising bars indicate increasing environmental impact, while declining bars suggest improved efficiency or cleaner energy adoption.", 
                          style={'fontSize': '13px', 'color': '#666', 'marginBottom': '15px'}),
                    dcc.Loading(dcc.Graph(id='ghg-emissions-bar-chart'))
                ])
            ], className="six columns"),
        ], className="row", style={'marginBottom': '20px'}),

        # Row 6: Correlation Heatmap & Energy Treemap
        html.Div([
            html.Div([
                html.Div(style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '8px', 'boxShadow': '0 2px 8px rgba(0,0,0,0.1)', 'height': '100%'}, children=[
                    html.H4("🔥 Energy Source Correlation (Heatmap)", style={'color': SECONDARY_COLOR, 'marginTop': '0'}),
                    html.P("Shows statistical correlations between selected energy sources. Values near +1 indicate sources that grow together, while -1 indicates inverse relationships. Requires at least 2 sources.", 
                          style={'fontSize': '13px', 'color': '#666', 'marginBottom': '15px'}),
                    dcc.Loading(dcc.Graph(id='energy-correlation-heatmap'))
                ])
            ], className="six columns"),
            html.Div([
                html.Div(style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '8px', 'boxShadow': '0 2px 8px rgba(0,0,0,0.1)', 'height': '100%'}, children=[
                    html.H4("🌳 Energy Breakdown (Treemap)", style={'color': SECONDARY_COLOR, 'marginTop': '0'}),
                    html.P("A hierarchical rectangle-based visualization showing the relative size of each selected energy source. Larger rectangles indicate greater consumption volumes.", 
                          style={'fontSize': '13px', 'color': '#666', 'marginBottom': '15px'}),
                    dcc.Loading(dcc.Graph(id='energy-treemap'))
                ])
            ], className="six columns"),
        ], className="row", style={'marginBottom': '20px'}),
    ]),

    # Footer
    html.Div(style={'backgroundColor': PRIMARY_COLOR, 'color': 'white', 'padding': '20px', 'marginTop': '40px', 'textAlign': 'center'}, children=[
        html.P("© 2025 World Energy Consumption Dashboard | Data Visualization Project", 
              style={'margin': '0', 'fontSize': '14px'}) 
    ])
])

# Callback for updating the graphs
@app.callback(
    [Output('energy-mix-pie-chart', 'figure'),
     Output('primary-energy-consumption-line-chart', 'figure'),
     Output('energy-correlation-heatmap', 'figure'),
     Output('global-energy-map', 'figure'),
     Output('energy-source-trend-chart', 'figure'),
     Output('stacked-area-chart', 'figure'),
     Output('stream-graph', 'figure'),
     Output('sunburst-chart', 'figure'),
     Output('gdp-vs-energy-scatter', 'figure'),
     Output('ghg-emissions-bar-chart', 'figure'),
     Output('energy-treemap', 'figure')],
    [Input('country-dropdown', 'value'),
     Input('year-slider', 'value'),
     Input('energy-source-checklist', 'value'),
     Input('map-projection-dropdown', 'value'),
     Input('map-metric-dropdown', 'value'),
     Input('map-percapita-toggle', 'value'),
     Input('map-year-slider', 'value'),
     Input('map-animate-toggle', 'value')]
)
def update_graphs(selected_country, selected_year, selected_energy_sources, map_projection, map_metric, percapita_toggle, map_year_value, map_animate_toggle):
    figures = [] 
    filtered_df = df[(df['country'] == selected_country) & 
                     (df['year'] >= selected_year[0]) & 
                     (df['year'] <= selected_year[1])]

    # ═══ Energy Mix Pie Chart ═══
    try:
        if not selected_energy_sources:
            pie_chart_figure = px.pie(
                values=[1], 
                names=['No Data'],
                title='Please Select At Least One Energy Source',
                template=CHART_TEMPLATE
            )
            pie_chart_figure.update_layout(showlegend=False)
        else:
            latest_year_df = filtered_df[filtered_df['year'] == filtered_df['year'].max()]
            
            if not latest_year_df.empty:
                energy_values = latest_year_df[selected_energy_sources].iloc[0].values
                energy_labels = [source.replace('_consumption', '').replace('_', ' ').title() for source in selected_energy_sources]

                pie_chart_figure = px.pie(
                    values=energy_values,
                    names=energy_labels,
                    title=f'Energy Mix for {selected_country} ({int(filtered_df["year"].max())})',
                    template=CHART_TEMPLATE,
                    color_discrete_sequence=px.colors.qualitative.Bold
                )
                pie_chart_figure.update_traces(
                    textposition='inside', 
                    textinfo='percent+label',
                    hovertemplate='<b>%{label}</b><br>Value: %{value:.2f} TWh<br>Percent: %{percent}<extra></extra>'
                )
            else:
                pie_chart_figure = px.pie(values=[1], names=['No Data'], title='No Data Available', template=CHART_TEMPLATE)
                pie_chart_figure.update_layout(showlegend=False)
    except Exception as e:
        pie_chart_figure = px.pie(values=[1], names=['Error'], title=f'Error: {str(e)}', template=CHART_TEMPLATE)
    figures.append(pie_chart_figure)

    # ═══ Primary Energy Consumption Line Chart ═══
    try: 
        energy_data = filtered_df[['year', 'primary_energy_consumption']].dropna()
        
        if energy_data.empty:
            line_chart_figure = px.line(
                title=f'Total Primary Energy Consumption - {selected_country} (No data available)',
                template=CHART_TEMPLATE
            )
            line_chart_figure.add_annotation(
                text="No primary energy consumption data available for selected period",
                xref="paper", yref="paper",
                x=0.5, y=0.5, showarrow=False,
                font=dict(size=14, color='gray')
            )
        else:
            line_chart_figure = px.line(
                energy_data,
                x='year',
                y='primary_energy_consumption',
                title=f'Total Primary Energy Consumption - {selected_country}',
                labels={'year': 'Year', 'primary_energy_consumption': 'Energy Consumption (TWh)'},
                template=CHART_TEMPLATE
            )
            line_chart_figure.update_traces(line_color=SECONDARY_COLOR, line_width=3)
            line_chart_figure.update_layout(hovermode='x unified', yaxis=dict(rangemode='tozero'))
    except Exception as e:
        line_chart_figure = {'layout': {'title': f'Error: {str(e)}', 'template': CHART_TEMPLATE}}
    figures.append(line_chart_figure)

    # ═══ Energy Source Correlation Heatmap ═══
    try:
        if not selected_energy_sources or len(selected_energy_sources) < 2:
            heatmap_figure = {'layout': {'title': 'Select At Least Two Energy Sources', 'template': CHART_TEMPLATE}}
        else: 
            correlation_data = filtered_df[selected_energy_sources].dropna()
            
            if len(correlation_data) < 2:
                heatmap_figure = {'layout': {'title': 'Insufficient data for correlation analysis', 'template': CHART_TEMPLATE}}
            else:
                correlation_df = correlation_data.corr()
                clean_labels = [label.replace('_consumption', '').replace('_', ' ').title() for label in selected_energy_sources]
                heatmap_figure = px.imshow(
                    correlation_df,
                    labels=dict(color="Correlation"),
                    x=clean_labels,
                    y=clean_labels,
                    title=f'Energy Source Correlation Matrix - {selected_country}',
                    template=CHART_TEMPLATE,
                    color_continuous_scale='RdBu_r',
                    aspect='auto'
                )
                heatmap_figure.update_layout(xaxis_title='Energy Source', yaxis_title='Energy Source')
    except Exception as e:
        heatmap_figure = {'layout': {'title': f'Error: {str(e)}', 'template': CHART_TEMPLATE}}
    figures.append(heatmap_figure)

    # ═══ Interactive Global Energy Map ═══
    try:
        # Configure selected energy metric and per-capita normalization
        metric_col = map_metric if map_metric else 'primary_energy_consumption'
        display_metric = metric_col.replace('_consumption', '').replace('_', ' ').title()
        normalize_per_capita = 'per_capita' in (percapita_toggle or [])

        # Prepare dataset based on animation mode (all years vs. single year)
        animate = 'animate' in (map_animate_toggle or [])
        if animate:
            map_data = df.copy()
            # Apply per-capita normalization  if enabled
            if normalize_per_capita and 'population' in map_data.columns:
                map_data = map_data[map_data['population'].notna()]
                map_data[metric_col] = (map_data[metric_col] / map_data['population']).replace([float('inf'), -float('inf')], float('nan'))

            map_data = map_data.dropna(subset=[metric_col])
        else:
            map_year = int(map_year_value) if map_year_value is not None else int(df['year'].max())
            map_data = df[df['year'] == map_year].copy()
            if normalize_per_capita and 'population' in map_data.columns:
                map_data = map_data[map_data['population'].notna()]
                map_data[metric_col] = (map_data[metric_col] / map_data['population']).replace([float('inf'), -float('inf')], float('nan'))
            map_data = map_data.dropna(subset=[metric_col])

        # Map visualization
        if map_projection == 'orthographic':
            # 3D globe visualization
            common_args = dict(
                locations='iso_code',
                color=metric_col,
                hover_name='country',
                hover_data={'gdp': ':,.0f', 'population': ':,.0f', 'iso_code': False, metric_col: ':.2f'},
                projection='orthographic',
                color_continuous_scale='Plasma',
                template=CHART_TEMPLATE,
                labels={
                    metric_col: f'{display_metric} (TWh)' if not normalize_per_capita else f'{display_metric} Per Capita',
                    'gdp': 'GDP',
                    'population': 'Population',
                    'country': 'Country'
                }
            )
            if animate:
                global_map_figure = px.scatter_geo(map_data, size=metric_col, animation_frame='year', **common_args)
            else:
                global_map_figure = px.scatter_geo(map_data, size=metric_col, **common_args)
            global_map_figure.update_layout(
                title=f"🌐 Global {display_metric}{' Per Capita' if normalize_per_capita else ''} - 3D Interactive Globe" + ('' if animate else f" ({int(map_year_value)})"),
                geo=dict(showland=True, showcountries=True, showocean=True, oceancolor='LightBlue', landcolor='rgb(243, 243, 243)', coastlinecolor='rgb(204, 204, 204)'),
                height=400, margin=dict(l=0, r=0, t=50, b=0)
            )
        else:
            #  2D choropleth map with country boundaries
            common_args2d = dict(
                locations='iso_code',
                color=metric_col,
                hover_name='country',
                hover_data={'iso_code': False, metric_col: ':.2f'},
                color_continuous_scale='YlOrRd',
                projection=map_projection,
                template=CHART_TEMPLATE,
                labels={
                    metric_col: f'{display_metric} (TWh)' if not normalize_per_capita else f'{display_metric} Per Capita',
                    'country': 'Country'
                }
            )
            if animate:
                global_map_figure = px.choropleth(map_data, animation_frame='year', **common_args2d)
            else:
                global_map_figure = px.choropleth(map_data, **common_args2d)
            title_proj = map_projection.title() if isinstance(map_projection, str) else '2D'
            title_year = '' if animate else f" ({int(map_year_value)})"
            global_map_figure.update_layout(
                title=f"🗺️ Global {display_metric}{' Per Capita' if normalize_per_capita else ''} - {title_proj} Projection{title_year}",
                geo=dict(showframe=False, showcoastlines=True, projection_type=map_projection),
                height=400, margin=dict(l=0, r=0, t=50, b=0)
            )
    except Exception as e:
        global_map_figure = {'layout': {'title': f'Error: {str(e)}', 'template': CHART_TEMPLATE}}
    figures.append(global_map_figure)

    # ═══ Energy Source Trends ═══
    try:
        if not selected_energy_sources:
            trend_chart_figure = {'layout': {'title': 'Select Energy Sources', 'template': CHART_TEMPLATE}}
        else: 
            trend_data = filtered_df[['year'] + selected_energy_sources].dropna(subset=selected_energy_sources, how='all')
            
            if trend_data.empty:
                trend_chart_figure = {'layout': {'title': 'No data available for selected sources', 'template': CHART_TEMPLATE}}
            else:
                trend_df = trend_data.melt(id_vars=['year'], value_vars=selected_energy_sources, 
                                            var_name='Energy Source', value_name='Consumption')
  
                trend_df = trend_df.dropna(subset=['Consumption'])
                trend_df['Energy Source'] = trend_df['Energy Source'].str.replace('_consumption', '').str.replace('_', ' ').str.title()
                
                trend_chart_figure = px.line(
                    trend_df,
                    x='year',
                    y='Consumption',
                    color='Energy Source',
                    title=f'Energy Source Consumption Trends - {selected_country}',
                    labels={'year': 'Year', 'Consumption': 'Consumption (TWh)', 'Energy Source': 'Energy Source'},
                    template=CHART_TEMPLATE,
                    color_discrete_sequence=px.colors.qualitative.Bold
                )
                trend_chart_figure.update_traces(line_width=2.5)
                trend_chart_figure.update_layout(hovermode='x unified', legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1), yaxis=dict(rangemode='tozero'))
    except Exception as e:
        trend_chart_figure = {'layout': {'title': f'Error: {str(e)}', 'template': CHART_TEMPLATE}}
    figures.append(trend_chart_figure)

    # ═══ Stacked Energy Composition ═══
    try:
        if not selected_energy_sources:
            stacked_area_fig = {'layout': {'title': 'Select Energy Sources', 'template': CHART_TEMPLATE}}
        else: 
            stacked_data = filtered_df[['year'] + selected_energy_sources].dropna(subset=selected_energy_sources, how='all')
            
            if stacked_data.empty:
                stacked_area_fig = {'layout': {'title': 'No data available for selected sources', 'template': CHART_TEMPLATE}}
            else:
                stacked_area_df = stacked_data.melt(id_vars='year', var_name='Energy Source', value_name='Consumption')

                stacked_area_df = stacked_area_df.dropna(subset=['Consumption'])
                stacked_area_df['Energy Source'] = stacked_area_df['Energy Source'].str.replace('_consumption', '').str.replace('_', ' ').str.title()
                stacked_area_fig = px.area(
                    stacked_area_df,
                    x='year',
                    y='Consumption',
                    color='Energy Source',
                    title=f'Stacked Energy Consumption - {selected_country}',
                    labels={'year': 'Year', 'Consumption': 'Consumption (TWh)', 'Energy Source': 'Energy Source'},
                    template=CHART_TEMPLATE,
                    color_discrete_sequence=px.colors.qualitative.Bold
                )
                stacked_area_fig.update_layout(hovermode='x unified', legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1), yaxis=dict(rangemode='tozero'))
    except Exception as e:
        stacked_area_fig = {'layout': {'title': f'Error: {str(e)}', 'template': CHART_TEMPLATE}}
    figures.append(stacked_area_fig)

    # ═══ Proportional Energy Mix Stream Graph ═══
    try:
        if not selected_energy_sources:
            stream_fig = {'layout': {'title': 'Select Energy Sources', 'template': CHART_TEMPLATE}}
        else: 
            stream_data = filtered_df[['year'] + selected_energy_sources].dropna(subset=selected_energy_sources, how='all')
            
            if stream_data.empty:
                stream_fig = {'layout': {'title': 'No data available for selected sources', 'template': CHART_TEMPLATE}}
            else:
                stream_df = stream_data.melt(id_vars='year', var_name='Energy Source', value_name='Consumption')

                stream_df = stream_df.dropna(subset=['Consumption'])
                stream_df['Energy Source'] = stream_df['Energy Source'].str.replace('_consumption', '').str.replace('_', ' ').str.title()
                stream_fig = px.area(
                    stream_df,
                    x='year',
                    y='Consumption',
                    color='Energy Source',
                    groupnorm='fraction',
                    title=f'Proportional Energy Mix Over Time - {selected_country}',
                    labels={'year': 'Year', 'Consumption': 'Proportion', 'Energy Source': 'Energy Source'},
                    template=CHART_TEMPLATE,
                    color_discrete_sequence=px.colors.qualitative.Bold
                )
                stream_fig.update_layout(hovermode='x unified', yaxis_tickformat='.0%', legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
    except Exception as e:
        stream_fig = {'layout': {'title': f'Error: {str(e)}', 'template': CHART_TEMPLATE}}
    figures.append(stream_fig)

    # ═══ Energy Mix Hierarchy (Sunburst) ═══
    try:
        if not selected_energy_sources:
            sunburst_fig = {'layout': {'title': 'Select Energy Sources', 'template': CHART_TEMPLATE}}
        else:
            sb_latest = filtered_df[filtered_df['year'] == filtered_df['year'].max()]
            if sb_latest.empty:
                sunburst_fig = {'layout': {'title': 'No Data Available', 'template': CHART_TEMPLATE}}
            else:
                sb_melt = sb_latest[selected_energy_sources]
                sb_series = sb_melt.iloc[0]
                sb_df = sb_series.reset_index()
                sb_df.columns = ['Energy Source', 'Consumption']
                sb_df['Energy Source'] = sb_df['Energy Source'].str.replace('_consumption', '').str.replace('_', ' ').str.title()
                sb_df['All'] = 'Total Energy'
                sunburst_fig = px.sunburst(
                    sb_df,
                    path=['All', 'Energy Source'],
                    values='Consumption',
                    title=f'Energy Mix Sunburst - {selected_country} ({int(filtered_df["year"].max())})',
                    labels={'Consumption': 'Consumption (TWh)', 'Energy Source': 'Energy Source'},
                    template=CHART_TEMPLATE,
                    color_discrete_sequence=px.colors.qualitative.Bold
                )
                sunburst_fig.update_traces(
                    hovertemplate='<b>%{label}</b><br>Value: %{value:.2f} TWh<br>Percent of Total: %{percentRoot}<extra></extra>'
                )
    except Exception as e:
        sunburst_fig = {'layout': {'title': f'Error: {str(e)}', 'template': CHART_TEMPLATE}}
    figures.append(sunburst_fig)

    # ═══ GDP vs Energy Consumption (Scatter) ═══
    try: 
        scatter_data = filtered_df[['year', 'gdp', 'primary_energy_consumption']].dropna().copy()
        
        if scatter_data.empty:
            scatter_fig = px.scatter(
                title=f"GDP vs. Energy Consumption - {selected_country} ",
                template=CHART_TEMPLATE
            )
            scatter_fig.add_annotation(
                text="No GDP or energy data available for selected period",
                xref="paper", yref="paper",
                x=0.5, y=0.5, showarrow=False,
                font=dict(size=14, color='gray')
            )
        else: 
            scatter_data['year_label'] = scatter_data['year'].astype(int).astype(str)
            
            scatter_fig = px.scatter(
                scatter_data,
                x="gdp",
                y="primary_energy_consumption",
                hover_data={'year': True, 'gdp': ':,.0f', 'primary_energy_consumption': ':.2f', 'year_label': False},
                title=f"GDP vs. Energy Consumption - {selected_country} ({len(scatter_data)} data points)",
                labels={
                    'gdp': 'GDP ($)', 
                    'primary_energy_consumption': 'Energy Consumption (TWh)', 
                    'year': 'Year'
                },
                template=CHART_TEMPLATE
            )
            scatter_fig.update_traces(
                marker=dict(size=20, color=SECONDARY_COLOR, line=dict(width=2, color='white'), opacity=0.8),
                mode='markers+text',
                text=scatter_data['year_label'],
                textposition='top center',
                textfont=dict(size=11, color='#2C3E50')
            )
            scatter_fig.update_layout(
                showlegend=False,
                hovermode='closest',
                xaxis=dict(rangemode='tozero'),
                yaxis=dict(rangemode='tozero')
            )
    except Exception as e:
        scatter_fig = {'layout': {'title': f'Error: {str(e)}', 'template': CHART_TEMPLATE}}
    figures.append(scatter_fig)

    # ═══ Greenhouse Gas Emissions ═══
    try: 
        ghg_data = filtered_df[['year', 'greenhouse_gas_emissions']].dropna()
        
        if ghg_data.empty:
            ghg_fig = px.bar(
                title=f"Greenhouse Gas Emissions - {selected_country} (No data available)",
                template=CHART_TEMPLATE
            )
            ghg_fig.add_annotation(
                text="No greenhouse gas emissions data available for selected period",
                xref="paper", yref="paper",
                x=0.5, y=0.5, showarrow=False,
                font=dict(size=14, color='gray')
            )
        else:
            ghg_fig = px.bar(
                ghg_data,
                x="year",
                y="greenhouse_gas_emissions",
                title=f"Greenhouse Gas Emissions - {selected_country}",
                labels={'year': 'Year', 'greenhouse_gas_emissions': 'GHG Emissions (Million Tonnes CO₂)'},
                template=CHART_TEMPLATE
            )
            ghg_fig.update_traces(marker_color=ACCENT_COLOR)
            ghg_fig.update_layout(yaxis=dict(rangemode='tozero'))
    except Exception as e:
        ghg_fig = {'layout': {'title': f'Error: {str(e)}', 'template': CHART_TEMPLATE}}
    figures.append(ghg_fig)

    # ═══ Energy Breakdown (Treemap) ═══
    try:
        if not selected_energy_sources:
            treemap_fig = {'layout': {'title': 'Select Energy Sources', 'template': CHART_TEMPLATE}}
        else: 
            treemap_df = filtered_df.melt(id_vars=['country'], value_vars=selected_energy_sources, 
                                          var_name='Energy Source', value_name='Consumption')
            treemap_df = treemap_df.dropna(subset=['Consumption'])
            treemap_df = treemap_df[treemap_df['Consumption'] > 0]
            
            if treemap_df.empty:
                treemap_fig = {'layout': {'title': 'No data available for selected sources', 'template': CHART_TEMPLATE}}
            else:
                treemap_df['Energy Source'] = treemap_df['Energy Source'].str.replace('_consumption', '').str.replace('_', ' ').str.title()
                
                treemap_fig = px.treemap(
                    treemap_df,
                    path=[px.Constant(selected_country), 'Energy Source'],
                    values='Consumption',
                    title=f'Energy Consumption Treemap - {selected_country}',
                    labels={'Consumption': 'Consumption (TWh)', 'Energy Source': 'Energy Source'},
                    template=CHART_TEMPLATE,
                    color='Energy Source',
                    color_discrete_sequence=px.colors.qualitative.Bold
                )
                treemap_fig.update_traces(
                    textinfo="label+value+percent parent",
                    hovertemplate='<b>%{label}</b><br>Value: %{value:.2f} TWh<br>Percent of Total: %{percentRoot}<extra></extra>'
                )
    except Exception as e:
        treemap_fig = {'layout': {'title': f'Error: {str(e)}', 'template': CHART_TEMPLATE}}
    figures.append(treemap_fig)

    return figures
# ═══════════════════════════════════════
# Launch Dash application server
# ═══════════════════════════════════════
if __name__ == '__main__':
    app.run(debug=False)
