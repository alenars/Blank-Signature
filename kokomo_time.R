Kokomo71$year <- as.Date(cut(Kokomo71$date,
                              breaks = "year"))
Kokomo71$month <- as.Date(cut(Kokomo71$date,
                              breaks = "month"))
Kokomo71$week <- as.Date(cut(Kokomo71$date,
                             breaks = "week",
                             start.on.monday = FALSE)) # changes weekly break point to Sunday

# graph by year:
ggplot(data = Kokomo71,
       aes(year, feet)) +
  stat_summary(fun.y = "mean", # adds up all observations for the month
               geom = "line") + # or "line"
  scale_x_date(date_labels = "%Y", date_breaks = "1 year")

ggplot(data = Kokomo71,
       aes(year, feet)) +
  stat_summary(fun.y = "mean", # adds up all observations for the month
               geom = "bar") + # or "line"
  scale_x_date(date_labels = "%Y", date_breaks = "1 year")

# graph by month:
ggplot(data = Kokomo71,
       aes(month, feet)) +
  stat_summary(fun.y = "mean", # adds up all observations for the month
               geom = "line") + # or "line"
  scale_x_date(date_labels = "%m/%Y", date_breaks = "month")

ggplot(data = Kokomo71,
       aes(month, feet)) +
  stat_summary(fun.y = "mean", # adds up all observations for the month
               geom = "bar") + # or "line"
  scale_x_date(date_labels = "%m/%Y", date_breaks = "1 month")

# graph by week:
ggplot(data = Kokomo71,
       aes(week, feet)) +
  stat_summary(fun.y = "mean", # adds up all observations for the week
               geom = "line") + # or "line"
  scale_x_date(
    labels = date_format("%d/%m/%Y"),
    breaks = "week")

ggplot(data = Kokomo71,
       aes(week, feet)) +
  stat_summary(fun.y = "mean", # adds up all observations for the week
               geom = "line") + # or "line"
  scale_x_date(date_labels = "%d/%m/%Y", date_breaks = "week")

plot(as.Date(Kokomo71$date,'%d/%m/%Y'),Kokomo71$feet, xlab="Date", ylab= "Feet", col='purple')

