# SQL and pandas comparison

## First SQL result: in-stock books

```text
                                                                                         title  price_gbp
                                                                          A Light in the Attic      51.77
                                                                            Tipping the Velvet      53.74
                                                                                    Soumission      50.10
                                                                                 Sharp Objects      47.82
                                                         Sapiens: A Brief History of Humankind      54.23
                                                                               The Requiem Red      22.65
                                            The Dirty Little Secrets of Getting Your Dream Job      33.34
       The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull      17.93
The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics      22.60
                                                                               The Black Maria      52.15
```

## SQL JOIN result

```text
 book_id                                                                                                                                                                           title  rating      category_name
       1                                                                                                                                                            A Light in the Attic       3             Poetry
       2                                                                                                                                                              Tipping the Velvet       1 Historical Fiction
       3                                                                                                                                                                      Soumission       1            Fiction
       4                                                                                                                                                                   Sharp Objects       4            Mystery
       5                                                                                                                                           Sapiens: A Brief History of Humankind       5            History
       6                                                                                                                                                                 The Requiem Red       1        Young Adult
       7                                                                                                                              The Dirty Little Secrets of Getting Your Dream Job       4           Business
       8                                                                                         The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull       3            Default
       9                                                                                  The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics       4            Default
      10                                                                                                                                                                 The Black Maria       1             Poetry
      11                                                                                                                                  Starving Hearts (Triangular Trade Trilogy, #1)       2            Default
      12                                                                                                                                                           Shakespeare's Sonnets       4             Poetry
      13                                                                                                                                                                     Set Me Free       5        Young Adult
      14                                                                                                                         Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)       5     Sequential Art
      15                                                                                                                                                       Rip it Up and Start Again       5              Music
      16                                                                                              Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991       3              Music
      17                                                                                                                                                                            Olio       1             Poetry
      18                                                                                                                           Mesaerion: The Best Science Fiction Stories 1800-1849       1    Science Fiction
      19                                                                                                                                                    Libertarianism for Beginners       2           Politics
      20                                                                                                                                                         It's Only the Himalayas       2             Travel
      21                                                                                                                                                                     In Her Wake       1           Thriller
      22                                                                                                                                                                 How Music Works       2              Music
      23 Foolproof Preserving: A Guide to Small Batch Jams, Jellies, Pickles, Condiments, and More: A Foolproof Guide to Making Small Batch Jams, Jellies, Pickles, Condiments, and More       3     Food and Drink
      24                                                                                                                                                      Chase Me (Paris Nights #2)       5            Romance
      25                                                                                                                                                                      Black Dust       5            Romance
      26                                                                                                                                                   Birdsong: A Story in Pictures       3          Childrens
      27                                                                     America's Cradle of Quarterbacks: Western Pennsylvania's Football Factory from Johnny Unitas to Joe Montana       3            Default
      28                                                                                                                                                  Aladdin and His Wonderful Lamp       3            Default
      29                                                                                                                         Worlds Elsewhere: Journeys Around Shakespeareâs Globe       5         Nonfiction
      30                                                                                                                                                                  Wall and Piece       4                Art
      31                                                                                                                      The Four Agreements: A Practical Guide to Personal Freedom       5       Spirituality
      32                                                                                                       The Five Love Languages: How to Express Heartfelt Commitment to Your Mate       3         Nonfiction
      33                                                                                                                                                               The Elephant Tree       5           Thriller
      34                                                                                                                                                          The Bear and the Piano       1          Childrens
      35                                                                                                                                                                  Sophie's World       5         Philosophy
      36                                                                                                                                                                     Penny Maybe       3            Default
      37                                                                                                                                  Maude (1883-1993):She Grew Up with the country       2            Default
      38                                                                                                                                                            In a Dark, Dark Wood       1            Mystery
      39                                                                                                                                                             Behind Closed Doors       4           Thriller
      40                                                                                                                                                  You can't bury them all: Poems       2             Poetry
      41                                                                                                                                                  Slow States of Collapse: Poems       3             Poetry
      42                                                                                                                                                           Reasons to Stay Alive       2         Nonfiction
      43                                                                                                                                                     Private Paris (Private #10)       5            Fiction
      44                                                                                                              #HigherSelfie: Wake Up Your Life. Free Your Soul. Find Your Tribe.       5         Nonfiction
      45                                                                                                                                                 Without Borders (Wanderlove #1)       2          New Adult
      46                                                                                                                                                                When We Collided       1       Contemporary
      47                                                                                                                                                    We Love You, Charlie Freeman       5            Fiction
      48                                                                                                                                         Untitled Collection: Sabbath Poems 2014       4             Poetry
      49                                                                       Unseen City: The Majesty of Pigeons, the Discreet Charm of Snails & Other Wonders of the Urban Wilderness       4         Nonfiction
      50                                                                                                                                                                  Unicorn Tracks       3            Fantasy
      51                                                                          Unbound: How Eight Technologies Made Us Human, Transformed Society, and Brought Our World to the Brink       1            History
      52                                                                                                                         Tsubasa: WoRLD CHRoNiCLE 2 (Tsubasa WoRLD CHRoNiCLE #2)       1     Sequential Art
      53                                                                                                     Throwing Rocks at the Google Bus: How Growth Became the Enemy of Prosperity       3         Nonfiction
      54                                                                                                                                                                 This One Summer       4     Sequential Art
      55                                                                                                                                                                          Thirst       5            Fiction
      56                                                                                                                                     The Torch Is Passed: A Harding Family Story       1      Add a comment
      57                                                                                                                                                 The Secret of Dreadwillow Carse       1          Childrens
      58                                                 The Pioneer Woman Cooks: Dinnertime: Comfort Classics, Freezer Food, 16-Minute Meals, and Other Delicious Ways to Solve Supper!       1     Food and Drink
      59                                                                                                                                                             The Past Never Ends       4            Mystery
      60                                                                                                                       The Natural History of Us (The Fine Art of Pretending #2)       3        Young Adult
      61                                                                                                                                        The Nameless City (The Nameless City #1)       4     Sequential Art
      62                                                                                                                               The Murder That Never Was (Forensic Instincts #5)       3            Fiction
      63                                                                                                                       The Most Perfect Thing: Inside (and Outside) a Bird's Egg       4            Science
      64                          The Mindfulness and Acceptance Workbook for Anxiety: A Guide to Breaking Free from Anxiety, Phobias, and Worry Using Acceptance and Commitment Therapy       4      Add a comment
      65                                                                                          The Life-Changing Magic of Tidying Up: The Japanese Art of Decluttering and Organizing       3         Nonfiction
      66                                                                                              The Inefficiency Assassin: Time Management Tactics for Working Smarter, Not Longer       5            Default
      67                                                                                                                       The Gutsy Girl: Escapades for Your Life of Epic Adventure       1         Nonfiction
      68                                                                                                                  The Electric Pencil: Drawings from Inside State Hospital No. 3       1         Nonfiction
      69                                                                                                                                    The Death of Humanity: and the Case for Life       4         Philosophy
      70                                                                                     The Bulletproof Diet: Lose up to a Pound a Day, Reclaim Energy and Focus, Upgrade Your Life       3             Health
      71                                                                                                                                                                  The Art Forger       3      Add a comment
      72                                                                                                     The Age of Genius: The Seventeenth Century and the Birth of the Modern Mind       1            History
      73                                                                                                             The Activist's Tao Te Ching: Ancient Advice for a Modern Revolution       5       Spirituality
      74                                                                                                  Spark Joy: An Illustrated Master Class on the Art of Organizing and Tidying Up       4         Nonfiction
      75                                                                                                                                                                     Soul Reader       2            Default
      76                                                                                                                                                                        Security       2             Horror
      77                                                                                                                                   Saga, Volume 6 (Saga (Collected Editions) #6)       3            Fantasy
      78                                                                                                                                   Saga, Volume 5 (Saga (Collected Editions) #5)       2     Sequential Art
      79                                                                                                               Reskilling America: Learning to Labor in the Twenty-First Century       2         Nonfiction
      80                                                                                                             Rat Queens, Vol. 3: Demons (Rat Queens (Collected Editions) #11-15)       3     Sequential Art
      81                                                                                               Princess Jellyfish 2-in-1 Omnibus, Vol. 01 (Princess Jellyfish 2-in-1 Omnibus #1)       5     Sequential Art
      82                                                                                                                                Princess Between Worlds (Wide-Awake Princess #5)       5            Fantasy
      83                                                                                                                                                     Pop Gun War, Volume 1: Gift       1     Sequential Art
      84             Political Suicide: Missteps, Peccadilloes, Bad Calls, Backroom Hijinx, Sordid Pasts, Rotten Breaks, and Just Plain Dumb Mistakes in the Annals of American Politics       2            History
      85                                                                                                                                                                        Patience       3     Sequential Art
      86                                                                                                                          Outcast, Vol. 1: A Darkness Surrounds Him (Outcast #1)       4     Sequential Art
      87                                                                                                          orange: The Complete Collection 1 (orange: The Complete Collection #1)       1     Sequential Art
      88                                                                                                                         Online Marketing for Busy Authors: A Step-By-Step Guide       1          Self Help
      89                                                                                                                                                             On a Midnight Clear       3      Add a comment
      90                                                                                                                                                               Obsidian (Lux #1)       2        Young Adult
      91                                                                                                                                           My Paris Kitchen: Recipes and Stories       2     Food and Drink
      92                                                                                                                                                               Masks and Shadows       2            Fantasy
      93                                                                                             Mama Tried: Traditional Italian Cooking for the Screwed, Crude, Vegan, and Tattooed       4     Food and Drink
      94                                                                                                                   Lumberjanes, Vol. 2: Friendship to the Max (Lumberjanes #5-8)       2     Sequential Art
      95                                                                                                                  Lumberjanes, Vol. 1: Beware the Kitten Holy (Lumberjanes #1-4)       3     Sequential Art
      96                                                                                                                         Lumberjanes Vol. 3: A Terrible Plan (Lumberjanes #9-12)       2     Sequential Art
      97                                                                                                                        Layered: Baking, Building, and Styling Spectacular Cakes       1     Food and Drink
      98                                                                                                           Judo: Seven Steps to Black Belt (an Introductory Guide for Beginners)       2      Add a comment
      99                                                                                                                                                                            Join       5    Science Fiction
     100                                                                                                                                       In the Country We Love: My Family Divided       4         Nonfiction
```

## pandas merge result

```text
 book_id                                                                                                                                                                           title  rating      category_name
       1                                                                                                                                                            A Light in the Attic       3             Poetry
       2                                                                                                                                                              Tipping the Velvet       1 Historical Fiction
       3                                                                                                                                                                      Soumission       1            Fiction
       4                                                                                                                                                                   Sharp Objects       4            Mystery
       5                                                                                                                                           Sapiens: A Brief History of Humankind       5            History
       6                                                                                                                                                                 The Requiem Red       1        Young Adult
       7                                                                                                                              The Dirty Little Secrets of Getting Your Dream Job       4           Business
       8                                                                                         The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull       3            Default
       9                                                                                  The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics       4            Default
      10                                                                                                                                                                 The Black Maria       1             Poetry
      11                                                                                                                                  Starving Hearts (Triangular Trade Trilogy, #1)       2            Default
      12                                                                                                                                                           Shakespeare's Sonnets       4             Poetry
      13                                                                                                                                                                     Set Me Free       5        Young Adult
      14                                                                                                                         Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)       5     Sequential Art
      15                                                                                                                                                       Rip it Up and Start Again       5              Music
      16                                                                                              Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991       3              Music
      17                                                                                                                                                                            Olio       1             Poetry
      18                                                                                                                           Mesaerion: The Best Science Fiction Stories 1800-1849       1    Science Fiction
      19                                                                                                                                                    Libertarianism for Beginners       2           Politics
      20                                                                                                                                                         It's Only the Himalayas       2             Travel
      21                                                                                                                                                                     In Her Wake       1           Thriller
      22                                                                                                                                                                 How Music Works       2              Music
      23 Foolproof Preserving: A Guide to Small Batch Jams, Jellies, Pickles, Condiments, and More: A Foolproof Guide to Making Small Batch Jams, Jellies, Pickles, Condiments, and More       3     Food and Drink
      24                                                                                                                                                      Chase Me (Paris Nights #2)       5            Romance
      25                                                                                                                                                                      Black Dust       5            Romance
      26                                                                                                                                                   Birdsong: A Story in Pictures       3          Childrens
      27                                                                     America's Cradle of Quarterbacks: Western Pennsylvania's Football Factory from Johnny Unitas to Joe Montana       3            Default
      28                                                                                                                                                  Aladdin and His Wonderful Lamp       3            Default
      29                                                                                                                         Worlds Elsewhere: Journeys Around Shakespeareâs Globe       5         Nonfiction
      30                                                                                                                                                                  Wall and Piece       4                Art
      31                                                                                                                      The Four Agreements: A Practical Guide to Personal Freedom       5       Spirituality
      32                                                                                                       The Five Love Languages: How to Express Heartfelt Commitment to Your Mate       3         Nonfiction
      33                                                                                                                                                               The Elephant Tree       5           Thriller
      34                                                                                                                                                          The Bear and the Piano       1          Childrens
      35                                                                                                                                                                  Sophie's World       5         Philosophy
      36                                                                                                                                                                     Penny Maybe       3            Default
      37                                                                                                                                  Maude (1883-1993):She Grew Up with the country       2            Default
      38                                                                                                                                                            In a Dark, Dark Wood       1            Mystery
      39                                                                                                                                                             Behind Closed Doors       4           Thriller
      40                                                                                                                                                  You can't bury them all: Poems       2             Poetry
      41                                                                                                                                                  Slow States of Collapse: Poems       3             Poetry
      42                                                                                                                                                           Reasons to Stay Alive       2         Nonfiction
      43                                                                                                                                                     Private Paris (Private #10)       5            Fiction
      44                                                                                                              #HigherSelfie: Wake Up Your Life. Free Your Soul. Find Your Tribe.       5         Nonfiction
      45                                                                                                                                                 Without Borders (Wanderlove #1)       2          New Adult
      46                                                                                                                                                                When We Collided       1       Contemporary
      47                                                                                                                                                    We Love You, Charlie Freeman       5            Fiction
      48                                                                                                                                         Untitled Collection: Sabbath Poems 2014       4             Poetry
      49                                                                       Unseen City: The Majesty of Pigeons, the Discreet Charm of Snails & Other Wonders of the Urban Wilderness       4         Nonfiction
      50                                                                                                                                                                  Unicorn Tracks       3            Fantasy
      51                                                                          Unbound: How Eight Technologies Made Us Human, Transformed Society, and Brought Our World to the Brink       1            History
      52                                                                                                                         Tsubasa: WoRLD CHRoNiCLE 2 (Tsubasa WoRLD CHRoNiCLE #2)       1     Sequential Art
      53                                                                                                     Throwing Rocks at the Google Bus: How Growth Became the Enemy of Prosperity       3         Nonfiction
      54                                                                                                                                                                 This One Summer       4     Sequential Art
      55                                                                                                                                                                          Thirst       5            Fiction
      56                                                                                                                                     The Torch Is Passed: A Harding Family Story       1      Add a comment
      57                                                                                                                                                 The Secret of Dreadwillow Carse       1          Childrens
      58                                                 The Pioneer Woman Cooks: Dinnertime: Comfort Classics, Freezer Food, 16-Minute Meals, and Other Delicious Ways to Solve Supper!       1     Food and Drink
      59                                                                                                                                                             The Past Never Ends       4            Mystery
      60                                                                                                                       The Natural History of Us (The Fine Art of Pretending #2)       3        Young Adult
      61                                                                                                                                        The Nameless City (The Nameless City #1)       4     Sequential Art
      62                                                                                                                               The Murder That Never Was (Forensic Instincts #5)       3            Fiction
      63                                                                                                                       The Most Perfect Thing: Inside (and Outside) a Bird's Egg       4            Science
      64                          The Mindfulness and Acceptance Workbook for Anxiety: A Guide to Breaking Free from Anxiety, Phobias, and Worry Using Acceptance and Commitment Therapy       4      Add a comment
      65                                                                                          The Life-Changing Magic of Tidying Up: The Japanese Art of Decluttering and Organizing       3         Nonfiction
      66                                                                                              The Inefficiency Assassin: Time Management Tactics for Working Smarter, Not Longer       5            Default
      67                                                                                                                       The Gutsy Girl: Escapades for Your Life of Epic Adventure       1         Nonfiction
      68                                                                                                                  The Electric Pencil: Drawings from Inside State Hospital No. 3       1         Nonfiction
      69                                                                                                                                    The Death of Humanity: and the Case for Life       4         Philosophy
      70                                                                                     The Bulletproof Diet: Lose up to a Pound a Day, Reclaim Energy and Focus, Upgrade Your Life       3             Health
      71                                                                                                                                                                  The Art Forger       3      Add a comment
      72                                                                                                     The Age of Genius: The Seventeenth Century and the Birth of the Modern Mind       1            History
      73                                                                                                             The Activist's Tao Te Ching: Ancient Advice for a Modern Revolution       5       Spirituality
      74                                                                                                  Spark Joy: An Illustrated Master Class on the Art of Organizing and Tidying Up       4         Nonfiction
      75                                                                                                                                                                     Soul Reader       2            Default
      76                                                                                                                                                                        Security       2             Horror
      77                                                                                                                                   Saga, Volume 6 (Saga (Collected Editions) #6)       3            Fantasy
      78                                                                                                                                   Saga, Volume 5 (Saga (Collected Editions) #5)       2     Sequential Art
      79                                                                                                               Reskilling America: Learning to Labor in the Twenty-First Century       2         Nonfiction
      80                                                                                                             Rat Queens, Vol. 3: Demons (Rat Queens (Collected Editions) #11-15)       3     Sequential Art
      81                                                                                               Princess Jellyfish 2-in-1 Omnibus, Vol. 01 (Princess Jellyfish 2-in-1 Omnibus #1)       5     Sequential Art
      82                                                                                                                                Princess Between Worlds (Wide-Awake Princess #5)       5            Fantasy
      83                                                                                                                                                     Pop Gun War, Volume 1: Gift       1     Sequential Art
      84             Political Suicide: Missteps, Peccadilloes, Bad Calls, Backroom Hijinx, Sordid Pasts, Rotten Breaks, and Just Plain Dumb Mistakes in the Annals of American Politics       2            History
      85                                                                                                                                                                        Patience       3     Sequential Art
      86                                                                                                                          Outcast, Vol. 1: A Darkness Surrounds Him (Outcast #1)       4     Sequential Art
      87                                                                                                          orange: The Complete Collection 1 (orange: The Complete Collection #1)       1     Sequential Art
      88                                                                                                                         Online Marketing for Busy Authors: A Step-By-Step Guide       1          Self Help
      89                                                                                                                                                             On a Midnight Clear       3      Add a comment
      90                                                                                                                                                               Obsidian (Lux #1)       2        Young Adult
      91                                                                                                                                           My Paris Kitchen: Recipes and Stories       2     Food and Drink
      92                                                                                                                                                               Masks and Shadows       2            Fantasy
      93                                                                                             Mama Tried: Traditional Italian Cooking for the Screwed, Crude, Vegan, and Tattooed       4     Food and Drink
      94                                                                                                                   Lumberjanes, Vol. 2: Friendship to the Max (Lumberjanes #5-8)       2     Sequential Art
      95                                                                                                                  Lumberjanes, Vol. 1: Beware the Kitten Holy (Lumberjanes #1-4)       3     Sequential Art
      96                                                                                                                         Lumberjanes Vol. 3: A Terrible Plan (Lumberjanes #9-12)       2     Sequential Art
      97                                                                                                                        Layered: Baking, Building, and Styling Spectacular Cakes       1     Food and Drink
      98                                                                                                           Judo: Seven Steps to Black Belt (an Introductory Guide for Beginners)       2      Add a comment
      99                                                                                                                                                                            Join       5    Science Fiction
     100                                                                                                                                       In the Country We Love: My Family Divided       4         Nonfiction
```

Both results are equivalent. The comparison passed using pd.testing.assert_frame_equal().
