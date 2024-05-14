# movies_and_votes = [
#     ['Batman Begins', 5],
#     ['Dune', 4],
#     ['Reign of Fire', 1],
#     ['Knives Out', 8],
# ]

with open('Week12/12InClassNotesData.csv') as movies_and_votes:

    flop = ''
    flop_votes = -1
    # flop_votes = 999
    # flop_votes = movies_and_votes[0][1]

    hit = ''
    hit_votes = 0

    count = 0 # count = len(movies_and_votes)

    # header = next(movies_and_votes)
    header = movies_and_votes.readline()
    # print(movies_and_votes)
    for line in movies_and_votes:
        count += 1 # count =+ 1 will not work, that's not a valid operator
        movie = line.strip().split(',')
        title = movie[0]
        votes = int(movie[1])
        # print(f'{title} - {votes}')
        # Find Hit Movie
        if hit_votes < votes:
            hit_votes = votes
            hit = title
        
        # Find Flop Movie
        if flop_votes > votes or flop_votes == -1:
            flop_votes = votes
            flop = title
        # if flop_votes > votes:
            # flop_votes = votes
            # flop = title

print(f'\nThe hit movie is {hit} with {hit_votes} votes.')
print(f'The flop movie is {flop} with {flop_votes} votes.\n')
print(f'{count} movies were voted on.\n')