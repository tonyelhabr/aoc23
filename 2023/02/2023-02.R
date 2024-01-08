library(stringr)
library(purrr)
lines <- readLines(file.path('2023', '02', 'data', 'input.txt'))

line_parts <- lines |> 
  str_remove('^.*[:] ') |> 
  str_split(';') |> 
  map(\(.x) str_trim(.x)) |> 
  set_names(1:length(lines))

coalesce <- function(x, y) {
  ifelse(is.na(x), y, x)
}

extract_number <- function(x, color) {
  suppressWarnings(
    str_replace(x, sprintf('(^.*, )?(\\d+)( %s.*$)', color), '\\2') |> 
      as.integer() |> 
      coalesce(0)
  )
}

map_pluck_int <- function(x, el) {
  x |> map_int(\(.x) pluck(.x, el))
}

valid_games <- line_parts |> 
  map(
    \(sets) {
      parsed_sets <- map(
        sets,
        \(set) {
          list(
            'r' = extract_number(set, 'red'),
            'g' = extract_number(set, 'green'),
            'b' = extract_number(set, 'blue')
          )
        }
      )
      r <- map_pluck_int(parsed_sets, 'r')
      g <- map_pluck_int(parsed_sets, 'g')
      b <- map_pluck_int(parsed_sets, 'b')
      all(r <= 12L) & all(g <= 13L) & all(b <= 14L)
    }
  ) |> 
  keep(\(.x) isTRUE(.x))
sum(as.integer(names(valid_games))) ## not 2205, but 2101
