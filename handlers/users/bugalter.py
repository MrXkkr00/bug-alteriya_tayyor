from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from data.config import ADMINS
from loader import db, dp, bot


@dp.callback_query_handler(text_contains="qabul", user_id=ADMINS[1])
async def answer_boss11(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[5:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="qabul_qilindi", id=uid)
    jarayon_haqida1 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Tugatdim', callback_data=f"finish{uid}")
            ],
        ]
    )
    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"ðð»ââï¸ Mijoz : {user[1]} \nð Topshiriq : {user[3]}\nâMohirâ topshiriqni Qabul qildi")
    await bot.send_message(chat_id=ADMINS[1],
                           text=f"ðð»ââï¸ Mijoz : {user[1]} \nð Topshiriq : {user[3]}\nð± Mijoz raqami : {user[2]}",
                           reply_markup=jarayon_haqida1)


@dp.callback_query_handler(text_contains="finish", user_id=ADMINS[1])
async def answer_boss1(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[6:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="tugatildi", id=uid)
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"ðð»ââï¸ Mijoz : {user[1]} \nð Topshiriq : {user[3]}\nð± Mijoz raqami : {user[2]} \nâMohirâ topshiriqni tugatdi")
    await bot.send_message(chat_id=ADMINS[1], text=f"Katta Raxmat")


@dp.callback_query_handler(text_contains="qabul", user_id=ADMINS[2])
async def answer_boss122(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[5:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="qabul_qilindi", id=uid)
    jarayon_haqida12 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Tugatdim', callback_data=f"finish{uid}")
            ],
        ]
    )
    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"ðð»ââï¸ Mijoz : {user[1]} \nð Topshiriq : {user[3]}\nâIsomiddinâ topshiriqni Qabul qildi")
    await bot.send_message(chat_id=ADMINS[2],
                           text=f"ðð»ââï¸ Mijoz : {user[1]} \nð Topshiriq : {user[3]}\nð±Mijoz raqami : {user[2]}",
                           reply_markup=jarayon_haqida12)


@dp.callback_query_handler(text_contains="finish", user_id=ADMINS[2])
async def answer_boss12(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[6:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="tugatildi", id=uid)
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"ðð»ââï¸ Mijoz : {user[1]} \nð Topshiriq : {user[3]}\nð± Mijoz raqami : {user[2]} \nâIsomiddinâ topshiriqni tugatdi")
    await bot.send_message(chat_id=ADMINS[2], text=f"Katta Raxmat")


@dp.callback_query_handler(text_contains="qabul", user_id=ADMINS[3])
async def answer_boss133(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[5:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="qabul_qilindi", id=uid)
    jarayon_haqida13 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Tugatdim', callback_data=f"finish{uid}")
            ],
        ]
    )
    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"ðð»ââï¸ Mijoz : {user[1]} \nð Topshiriq : {user[3]}\nâZoxidâ topshiriqni Qabul qildi")
    await bot.send_message(chat_id=ADMINS[3],
                           text=f"ðð»ââï¸ Mijoz : {user[1]} \nð Topshiriq : {user[3]}\nð± Mijoz raqami : {user[2]}",
                           reply_markup=jarayon_haqida13)


@dp.callback_query_handler(text_contains="finish", user_id=ADMINS[3])
async def answer_boss13(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[6:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="tugatildi", id=uid)
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"ðð»ââï¸ Mijoz : {user[1]} \nð Topshiriq : {user[3]}\nð± Mijoz raqami : {user[2]} \nâZoxidâ topshiriqni tugatdi")
    await bot.send_message(chat_id=ADMINS[3], text=f"Katta Raxmat")


@dp.callback_query_handler(text_contains="qabul", user_id=ADMINS[4])
async def answer_boss244(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[5:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="qabul_qilindi", id=uid)
    jarayon_haqida14 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Tugatdim', callback_data=f"finish{uid}")
            ],
        ]
    )
    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"ðð»ââï¸ Mijoz : {user[1]} \nð Topshiriq : {user[3]}\nâIrodaâ topshiriqni Qabul qildi")
    await bot.send_message(chat_id=ADMINS[4],
                           text=f"ðð»ââï¸ Mijoz : {user[1]} \nð Topshiriq : {user[3]}\nð± Mijoz raqami : {user[2]}",
                           reply_markup=jarayon_haqida14)


@dp.callback_query_handler(text_contains="finish", user_id=ADMINS[4])
async def answer_boss14(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[6:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="tugatildi", id=uid)
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"ðð»ââï¸Mijoz : {user[1]} \nð Topshiriq : {user[2]}\nð±Mijoz raqami : {user[2]} \nâIrodaâ topshiriqni tugatdi")
    await bot.send_message(chat_id=ADMINS[4], text=f"Katta Raxmat")


@dp.callback_query_handler(text_contains="qabul", user_id=ADMINS[5])
async def answer_boss155(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[5:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="qabul_qilindi", id=uid)
    jarayon_haqida15 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Tugatdim', callback_data=f"finish{uid}")
            ],
        ]
    )
    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"ðð»ââï¸Mijoz : {user[1]} \nð Topshiriq : {user[3]}\nâBegzodâ topshiriqni Qabul qildi")
    await bot.send_message(chat_id=ADMINS[5],
                           text=f"ðð»ââï¸Mijoz : {user[1]} \nð Topshiriq : {user[3]}\nð± Mijoz raqami : {user[2]}",
                           reply_markup=jarayon_haqida15)


@dp.callback_query_handler(text_contains="finish", user_id=ADMINS[5])
async def answer_boss15(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[6:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="tugatildi", id=uid)
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"ðð»ââï¸ Mijoz : {user[1]} \nð Topshiriq : {user[3]}\nð± Mijoz raqami : {user[2]} \nâBegzodâ topshiriqni tugatdi")
    await bot.send_message(chat_id=ADMINS[5], text=f"Katta Raxmat")


@dp.callback_query_handler(text_contains="qabul", user_id=ADMINS[6])
async def answer_boss166(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[5:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="qabul_qilindi", id=uid)
    jarayon_haqida16 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Tugatdim', callback_data=f"finish{uid}")
            ],
        ]
    )
    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"ðð»ââï¸ Mijoz : {user[1]} \nð Topshiriq : {user[3]}\nâAzimâ topshiriqni Qabul qildi")
    await bot.send_message(chat_id=ADMINS[6],
                           text=f"ðð»ââï¸ Mijoz : {user[1]} \nð Topshiriq : {user[3]}\nð± Mijoz raqami : {user[2]}",
                           reply_markup=jarayon_haqida16)


@dp.callback_query_handler(text_contains="finish", user_id=ADMINS[6])
async def answer_boss16(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[6:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="tugatildi", id=uid)
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"ðð»ââï¸ Mijoz : {user[1]} \nð Topshiriq : {user[3]}\nð± Mijoz raqami : {user[2]} \nâAzimâ topshiriqni tugatdi")
    await bot.send_message(chat_id=ADMINS[6], text=f"Katta Raxmat")


@dp.callback_query_handler(text_contains="qabul", user_id=ADMINS[7])
async def answer_boss177(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[5:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="qabul_qilindi", id=uid)
    jarayon_haqida17 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Tugatdim', callback_data=f"finish{uid}")
            ],
        ]
    )
    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"ðð»ââï¸ Mijoz : {user[1]} \nð Topshiriq : {user[3]}\nâAbduraxmonâ topshiriqni Qabul qildi")
    await bot.send_message(chat_id=ADMINS[7],
                           text=f"ðð»ââï¸ Mijoz : {user[1]} \nð Topshiriq : {user[3]}\nð± Mijoz raqami : {user[2]}",
                           reply_markup=jarayon_haqida17)


@dp.callback_query_handler(text_contains="finish", user_id=ADMINS[7])
async def answer_boss17(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[6:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="tugatildi", id=uid)
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"ðð»ââï¸ Mijoz : {user[1]} \nð Topshiriq : {user[3]}\nð± Mijoz raqami : {user[2]} \nâAbduraxmonâ topshiriqni tugatdi")
    await bot.send_message(chat_id=ADMINS[7], text=f"Katta Raxmat")


@dp.callback_query_handler(text_contains="qabul", user_id=ADMINS[8])
async def answer_boss188(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[5:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="qabul_qilindi", id=uid)
    jarayon_haqida18 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Tugatdim', callback_data=f"finish{uid}")
            ],
        ]
    )
    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"ðð»ââï¸ Mijoz : {user[1]} \nð Topshiriq : {user[3]}\nâAbdulvositâ topshiriqni Qabul qildi")
    await bot.send_message(chat_id=ADMINS[8],
                           text=f"ðð»ââï¸ Mijoz : {user[1]} \nð Topshiriq : {user[3]}\nð± Mijoz raqami : {user[2]}",
                           reply_markup=jarayon_haqida18)


@dp.callback_query_handler(text_contains="finish", user_id=ADMINS[8])
async def answer_boss18(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[6:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="tugatildi", id=uid)
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"ðð»ââï¸ Mijoz : {user[1]} \nð Topshiriq : {user[3]}\nð± Mijoz raqami : {user[2]} \nâAbdulvositâ topshiriqni tugatdi")
    await bot.send_message(chat_id=ADMINS[8], text=f"Katta Raxmat")


@dp.callback_query_handler(text_contains="qabul", user_id=ADMINS[9])
async def answer_boss89(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[5:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="qabul_qilindi", id=uid)
    jarayon_haqida9 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Tugatdim', callback_data=f"finish{uid}")
            ],
        ]
    )
    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"ðð»ââï¸ Mijoz : {user[1]} \nð Topshiriq : {user[3]}\nâbug'alter1â topshiriqni Qabul qildi")
    await bot.send_message(chat_id=ADMINS[9],
                           text=f"ðð»ââï¸ Mijoz : {user[1]} \nð Topshiriq : {user[3]}\nð± Mijoz raqami : {user[2]}",
                           reply_markup=jarayon_haqida9)


@dp.callback_query_handler(text_contains="finish", user_id=ADMINS[9])
async def answer_boss9(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[6:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="tugatildi", id=uid)
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"ðð»ââï¸ Mijoz : {user[1]} \nð Topshiriq : {user[2]}\nð±Mijoz raqami : {user[2]} \nâbug'alter1â topshiriqni tugatdi")
    await bot.send_message(chat_id=ADMINS[9], text=f"Katta Raxmat")


@dp.callback_query_handler(text_contains="qabul", user_id=ADMINS[10])
async def answer_boss810(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[5:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="qabul_qilindi", id=uid)
    jarayon_haqida10 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Tugatdim', callback_data=f"finish{uid}")
            ],
        ]
    )
    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"ðð»ââï¸ Mijoz : {user[1]} \nð Topshiriq : {user[3]}\nâbug'alter2â topshiriqni Qabul qildi")
    await bot.send_message(chat_id=ADMINS[10],
                           text=f"ðð»ââï¸ Mijoz : {user[1]} \nð Topshiriq : {user[3]}\nð± Mijoz raqami : {user[2]}",
                           reply_markup=jarayon_haqida10)


@dp.callback_query_handler(text_contains="finish", user_id=ADMINS[10])
async def answer_boss10(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[6:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="tugatildi", id=uid)
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"ðð»ââï¸ Mijoz : {user[1]} \nð Topshiriq : {user[3]}\nð± Mijoz raqami : {user[2]} \nâbug'alter2â topshiriqni tugatdi")
    await bot.send_message(chat_id=ADMINS[10], text=f"Katta Raxmat")
