const express = require('express'); const app = express();
app.get('/ping', (_,res)=>res.json({status:'ok'}));
app.listen(3000, ()=>console.log('http://localhost:3000'));
