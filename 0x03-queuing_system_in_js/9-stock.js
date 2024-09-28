import express from 'express';
import { createClient } from 'redis';

const listProducts = [
  {
    id: 1,
    name: 'Suitcase 250',
    price: 50,
    stock: 4,
  },
  {
    id: 2,
    name: 'Suitcase 450',
    price: 100,
    stock: 10,
  },
  {
    id: 3,
    name: 'Suitcase 650',
    price: 350,
    stock: 2,
  },
  {
    id: 4,
    name: 'Suitcase 1050',
    price: 550,
    stock: 5,
  },
];

// data access client
const getItemById = (id) => {
  for (const product of listProducts) {
    if (product.id === parseInt(id)) {
      return product;
    }
  }
  return false;
};
const getAllProducts = () => {
  const responseArray = [];
  for (const product of listProducts) {
    const responseProduct = {
      itemId: product.id,
      itemName: product.name,
      price: product.price,
      initialAvailableQuantity: product.stock,
    };
    responseArray.push(responseProduct);
  }
  return responseArray;
};

const reserveStockById = async (itemId, stock) => {
  try {
    const responseStatus = await client.incr(itemId);
    return true;
  } catch (error) {
    return false;
  }
};
const getCurrentReservedStockById = async (itemId) => {
  try {
    const data = await client.get(itemId);
    return parseInt(data);
  } catch (err) {
    throw err;
  }
};

// express client
const app = express();
const port = 1245;

// routes
app.get('/list_products', (req, res) => {
  // function that gets all the products
  res.status(200);
  res.json(getAllProducts());
});

app.get('/list_products/:itemId', async (req, res) => {
  const item = getItemById(req.params.itemId);
  if (!item) {
    return res.json({
      status: 'Product not found',
    });
  }

  try {
    const storedStock = await getCurrentReservedStockById(req.params.itemId);
    return res.json({
      itemId: item.id,
      itemName: item.name,
      price: item.price,
      initialAvailableQuantity: item.stock,
      currentQuantity: item.stock - storedStock,
    });
  } catch (err) {
    console.log('Error when getting current reserved stock:', err.toString());
  }
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const item = getItemById(req.params.itemId);

  if (!item) {
    return res.json({
      status: 'Product not found',
    });
  }

  try {
    const reservedStock = await getCurrentReservedStockById(req.params.itemId);
    const currentStock = item.stock - reservedStock;
    if (currentStock === 0) {
      return res.json({
        status: 'Not enough stock available',
        itemId: item.id,
      });
    }

    const reserveStatus = await reserveStockById(req.params.itemId, 1);
    if (reserveStatus) {
      return res.json({
        status: 'Reservation confirmed',
        itemId: item.id,
      });
    }
  } catch (err) {
    console.log('Error in route GET reserve_product/:itemId', err.toString());
  }
});

// redis client
const client = createClient();

// event listeners
client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err);
});

client.on('connect', () => {
  // redis
  console.log('Redis client connected');

  // express
  app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
  });
});

client.connect();
