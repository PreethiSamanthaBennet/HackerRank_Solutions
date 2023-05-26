    int total_number_of_shelves;

    scanf("%d", &total_number_of_shelves);
    total_number_of_books = calloc(total_number_of_shelves,sizeof(int));
    
    int total_number_of_queries;
    scanf("%d", &total_number_of_queries);
    total_number_of_pages = malloc(total_number_of_shelves*sizeof(int *));
    for(int i = 0; i < total_number_of_shelves; i++){
        total_number_of_pages[i] = calloc(1100, sizeof(int));
    }
    while (total_number_of_queries--) {
        int type_of_query;
        scanf("%d", &type_of_query);
        
        if (type_of_query == 1) {
            int x, y;
            scanf("%d %d", &x, &y);
            
            total_number_of_books[x]++;

            int * book = total_number_of_pages[x];
            
            while(*book != NULL)
                book++;
            *book = y;
