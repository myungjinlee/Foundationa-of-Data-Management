select count(*) from action_view where action_view.customer_id not in (select * from horror_view where horror_view.customer_id);
