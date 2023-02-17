from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup

button = ReplyKeyboardMarkup(resize_keyboard=True,
                                keyboard=[
                                    [
                                        KeyboardButton(text='ish beruvchi'),
                                        KeyboardButton(text='ishchi'),
                                    ]
                                ]
                                    
                            )

keyboard = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton
(
    text ='Python',callback_data='Python'
    ),
    InlineKeyboardButton
(
    text ='Java',callback_data='Java'
    ),
        InlineKeyboardButton
(
    text ='C++',callback_data='C++'
    ),
        InlineKeyboardButton
(
    text ='JavaScript',callback_data='JavaScript'
    ),
    InlineKeyboardButton
(
    text ='HTML',callback_data='HTML'
    ),
    InlineKeyboardButton
(
    text ='CSS',callback_data='CSS'
    ),
    InlineKeyboardButton
(
    text ='SQL',callback_data='SQL'
    ),
    InlineKeyboardButton
(
    text ='C',callback_data='C'
    ),
    InlineKeyboardButton
(
    text ='TypeSript',callback_data='TypeScript'
    ),
    InlineKeyboardButton
(
    text ='Bash/Shell',callback_data='Bash/Shell'
    ),
        InlineKeyboardButton
(
    text ='Go',callback_data='Go'
    ),
     InlineKeyboardButton
(
    text ='Swift',callback_data='Swift'
    ),

)

