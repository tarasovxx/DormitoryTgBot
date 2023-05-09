# Всем привет вас привествует разработчик и админ магазиина общаг FoodUpstairs
- Основная концепция и задумка заключается в том, чтобы люди могли экономить, никуда не выходя из дома.
- Для этого мы разпаботали простого бота, который поможет людям взаимодействовать с магаизином.
- Чтобы люди могли круглосуточно делать заказы, а поставщики видели, что у них заказли и соответсвенно уже отправлялим/доставляли сам товар непосредственно заказчику.


# Ботя является полностью portable
- Инструкция по устаноке бота себе
```
1.  Install Python 3.9.7 https://www.python.org/downloads/release/python-397/

2.  REPLACE THE PATH to python.exe in create_venv.bat to your 

<<<<<<< HEAD
3.  Run create_venv.bat
4.  Add to Meta folder token.txt (TG-bot token) and admins.txt (list of admin ID)
5.  Run bot_run.bat
```
=======
## Home menu
![home_menu_purple](https://user-images.githubusercontent.com/99086730/163854200-4ede9147-ae99-47a2-9257-d20e5b6fa263.png)

## ⚙️ Functions

### 🎮 Choose game
After clicking on ```🎮 Choose game``` button the bot will send limited amount of the products from the database. Limit 5. 
Each message with product contains the image of a product, the name, price per day, price per week and the price of the deposit. 
Also under the message there are two Inline buttons ```Rent 'Game name' per day``` and ```Rent 'Game name' per week```. Both add the game to the cart.

![product_bg_white](https://user-images.githubusercontent.com/99086730/163853567-16d50359-bd1c-42e6-8fc4-73732a5e996e.png)

### ✉️ Suggest a game
Allows a user to suggest a game. The suggestion saves to the database. 

### 🖌 Ask
Allows a user to ask a question. The question automatically sends to the Admin chat.

### 🗑 Cart
After clicking on ```🗑 Cart``` button the bot will send a message with user's cart info and will display the Cart menu. In this menu user can  
```✂️ Delete from cart```, which basically deletes a particular item from cart. Also user can ```🟢 Checkout```.  
After that user will be able to choose between payment methods and delivery methods.
![cart_menu](https://user-images.githubusercontent.com/99086730/163855921-4837f0aa-9182-42a9-a33c-7788543dc231.png)

## 📟 Admin panel
An admin should create a new chat where he should add the bot. The bot will check if the admin is actually the admin of the chat and 
if so he will send a message with admin panel menu.
![admin_panel_menu](https://user-images.githubusercontent.com/99086730/163856717-37cc017e-32af-4477-b1a6-ae62eb69baa7.png)

### 📪 Set available
After clicking on ```📪 Set available``` button admin will be asked to write tha name of a game, which will be set available. After sending a message with the name
of the game, the bot will update the availability of the product in the database.

### 🎲 Add a game
After clicking on ```🎲 Add a game``` button admin will be asked to write some info about a new game to add. After following the steps the bot will add game
to the Database.

### 💥 Delete a game
After clicking on ```💥 Delete a game``` button admin will be asked to write the name of the game which he wants to delete. After that game will be deleted from 
the Database.

## 💳 Payment card
User can pay with a payment card. I used the Qiwi p2p to make this work. It just creates the bill and sends the url to user. After that user should click on 
``` Check payment ``` button. If he successfully payed the bill, order's will be saved to the Database and also will be send to the admin.
>>>>>>> b70dc7e (Update README.md)
