mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"srinath1412001@gmail.com.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\