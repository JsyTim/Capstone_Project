# Capstone_Project

## flask-sqlacodegen "mysql://root:@127.0.0.1/book_db" --tables user --outfile "common/models/user.py"  --flask


flask-sqlacodegen "mysql://root:123456@127.0.0.1/book_db" --tables app_error_log --outfile "common/models/log/app_error_log.py"  --flask

flask-sqlacodegen "mysql://root:123456@127.0.0.1/book_db" --tables app_access_log --outfile "common/models/log/app_access_log.py"  --flask

flask-sqlacodegen "mysql://root:123456@127.0.0.1/book_db" --tables book_sale_change_log --outfile "common/models/book/Book_sale_change_log.py"  --flask

flask-sqlacodegen "mysql://root:123456@127.0.0.1/book_db" --tables book_stock_change_log --outfile "common/models/book/Book_stock_change_log.py"  --flask

flask-sqlacodegen "mysql://root:123456@127.0.0.1/book_db" --tables book_cat --outfile "common/models/book/Book_cat.py"  --flask

flask-sqlacodegen "mysql://root:123456@127.0.0.1/book_db" --tables book --outfile "common/models/book/Book.py"  --flask

flask-sqlacodegen "mysql://root:123456@127.0.0.1/book_db" --tables member --outfile "common/models/member/Member"  --flask

flask-sqlacodegen "mysql://root:123456@127.0.0.1/book_db" --tables member_address --outfile "common/models/member/memberAddress.py"  --flask

flask-sqlacodegen "mysql://root:123456@127.0.0.1/book_db" --tables member_cart --outfile "common/models/member/memberCart.py"  --flask

flask-sqlacodegen "mysql://root:123456@127.0.0.1/book_db" --tables pay_order_item --outfile "common/models/pay/payOrderItem.py"  --flask


flask-sqlacodegen "mysql://root:123456@127.0.0.1/book_db" --tables pay_order_callback_data --outfile "common/models/pay/payOrderCallbackData.py"  --flask

flask-sqlacodegen "mysql://root:123456@127.0.0.1/book_db" --tables pay_order --outfile "common/models/pay/payOrder.py"  --flask

flask-sqlacodegen "mysql://root:123456@127.0.0.1/book_db" --tables member_comments --outfile "common/models/member/memberComments.py"  --flask

queue_list

flask-sqlacodegen "mysql://root:123456@127.0.0.1/book_db" --tables queue_list --outfile "common/models/queue/QueueList.py"  --flask

flask-sqlacodegen "mysql://root:123456@127.0.0.1/book_db" --tables stat_daily_book --outfile "common/models/stat/StatDailyBook.py"  --flask


flask-sqlacodegen "mysql://root:123456@127.0.0.1/book_db" --tables stat_daily_member --outfile "common/models/stat/StatDailyMember.py"  --flask


flask-sqlacodegen "mysql://root:123456@127.0.0.1/book_db" --tables stat_daily_site --outfile "common/models/stat/StatDailySite.py"  --flask


flask-sqlacodegen "mysql://root:123456@127.0.0.1/book_db" --tables oauth_member_bind --outfile "common/models/member/OauthMemberBind.py"  --flask