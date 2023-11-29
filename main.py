from azure.cosmos import CosmosClient, PartitionKey, exceptions

# Initialize Cosmos Client
url = "<your_cosmos_db_account_url>"
key = '<your_cosmos_db_account_key>'
client = CosmosClient(url, credential=key)

# Create a database
database_name = 'testDatabase'
database = client.create_database_if_not_exists(id=database_name)

# Create a container
container_name = 'products'
container = database.create_container_if_not_exists(
    id=container_name, 
    partition_key=PartitionKey(path="/productName"),
    offer_throughput=400
)

def create_item(product_name, description):
    product_item = {
        'id': '1',
        'productName': product_name,
        'description': description
    }
    container.create_item(body=product_item)

def read_item(product_name):
    item_response = container.read_item(item='1', partition_key=product_name)
    return item_response

def update_item(product_name, description):
    read_item = container.read_item(item='1', partition_key=product_name)
    read_item['description'] = description
    container.replace_item(item=read_item, body=read_item)

def delete_item(product_name):
    container.delete_item(item='1', partition_key=product_name)