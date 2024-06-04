# Build a query engine from the index
query_engine = index.as_query_engine()

# Execute a query and print the response
response = query_engine.query('Give me my calendar.')
print(response)
