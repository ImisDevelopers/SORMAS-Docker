FROM grafana/grafana:7.2.0

# https://grafana.com/docs/grafana/latest/administration/configuration/
# https://grafana.com/docs/grafana/latest/installation/configure-docker/
# https://grafana.com/docs/grafana/latest/features/datasources/postgres/

# Disable server reporting of telemetry data
ENV GF_ANALYTICS_REPORTING_ENABLED false

ENV GF_DASHBOARDS_DEFAULT_HOME_DASHBOARD_PATH /etc/grafana/provisioning/dashboards/home.json

COPY datasources/ /etc/grafana/provisioning/datasources/

COPY dashboards/ /etc/grafana/provisioning/dashboards/