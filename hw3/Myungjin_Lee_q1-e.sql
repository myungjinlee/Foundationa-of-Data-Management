select concat(first_name, " ", last_name) as actor_name 
from actor 
where actor.actor_id 
in 
(select distinct actor_id 
from film_actor 
group by actor_id 
having count(actor_id)>=2)
order by actor_name;
