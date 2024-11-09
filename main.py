# Developer : Pouria Hosseini | Telegram ID : @isPoori | CHANNEL : @OmgaDeveloper 
import json
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext

TOKEN = "Token" # TOKEN
ADMIN_ID = 6442202961  # ADMIN

DATABASE_FILE = "disease_db.json"


def load_disease_db():
    try:
        with open(DATABASE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save_disease_db(disease_db):
    with open(DATABASE_FILE, "w", encoding="utf-8") as f:
        json.dump(disease_db, f, ensure_ascii=False, indent=4)


ADD_NAME, ADD_DESCRIPTION, ADD_CAUSE, ADD_MEDICATIONS = range(4)


def start(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    if user_id == ADMIN_ID:
        update.message.reply_text("سلام ادمین! برای افزودن بیماری جدید از دستور /admin استفاده کنید.")
    else:
        update.message.reply_text("سلام! برای دریافت راهنمایی بیماری خود را ارسال کنید.")


def admin(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    if user_id == ADMIN_ID:
        keyboard = [
            [InlineKeyboardButton("اضافه کردن بیماری", callback_data="add_disease")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text("سلام ادمین! لطفاً یک گزینه انتخاب کنید:", reply_markup=reply_markup)
    else:
        update.message.reply_text("شما دسترسی به این بخش ندارید.")


def add_disease(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    if user_id == ADMIN_ID:
        update.callback_query.answer()  
        update.callback_query.edit_message_text("لطفاً نام بیماری جدید را وارد کنید.")
        return ADD_NAME
    else:
        update.message.reply_text("شما دسترسی به این بخش ندارید.")
        return ConversationHandler.END

def add_name(update: Update, context: CallbackContext):
    disease_name = update.message.text
    context.user_data['disease_name'] = disease_name
    update.message.reply_text("لطفاً توضیحات بیماری را وارد کنید.")
    return ADD_DESCRIPTION

def add_description(update: Update, context: CallbackContext):
    description = update.message.text
    disease_name = context.user_data['disease_name']
    disease_db = load_disease_db() 
    disease_db[disease_name] = {"description": description, "causes": [], "recommended_medications": []}
    save_disease_db(disease_db)  
    update.message.reply_text("لطفاً علت‌های بیماری را وارد کنید (با ویرگول جدا کنید).")
    return ADD_CAUSE

def add_cause(update: Update, context: CallbackContext):
    causes = update.message.text.split(",")
    disease_name = context.user_data['disease_name']
    disease_db = load_disease_db()  
    disease_db[disease_name]["causes"] = causes
    save_disease_db(disease_db) 
    update.message.reply_text("لطفاً داروهای پیشنهادی برای این بیماری را وارد کنید (با ویرگول جدا کنید).")
    return ADD_MEDICATIONS

def add_medications(update: Update, context: CallbackContext):
    medications = update.message.text.split(",")
    disease_name = context.user_data['disease_name']
    disease_db = load_disease_db()  
    disease_db[disease_name]["recommended_medications"] = medications
    save_disease_db(disease_db)  
    update.message.reply_text("بیماری جدید با موفقیت به دیتابیس اضافه شد.")
    return ConversationHandler.END

# دریافت اطلاعات بیماری از دیتابیس
def get_disease_info(update: Update, context: CallbackContext):
    user_input = update.message.text.lower()
    disease_db = load_disease_db()  
    for disease, details in disease_db.items():
        if disease.lower() in user_input:
            update.message.reply_text(f"بیماری: {disease}\n"
                                      f"توضیحات: {details['description']}\n"
                                      f"علل: {', '.join(details['causes'])}\n"
                                      f"داروهای پیشنهادی: {', '.join(details['recommended_medications'])}")
            return
    update.message.reply_text("بیماری مورد نظر پیدا نشد. لطفاً دوباره تلاش کنید.")


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    
    dp.add_handler(CommandHandler("start", start))
    
    
    dp.add_handler(CommandHandler("admin", admin))

    
    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('admin', admin), MessageHandler(Filters.regex('^add_disease$'), add_disease)],
        states={
            ADD_NAME: [MessageHandler(Filters.text & ~Filters.command, add_name)],
            ADD_DESCRIPTION: [MessageHandler(Filters.text & ~Filters.command, add_description)],
            ADD_CAUSE: [MessageHandler(Filters.text & ~Filters.command, add_cause)],
            ADD_MEDICATIONS: [MessageHandler(Filters.text & ~Filters.command, add_medications)],
        },
        fallbacks=[],
    )

    dp.add_handler(conversation_handler)
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, get_disease_info))

    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()