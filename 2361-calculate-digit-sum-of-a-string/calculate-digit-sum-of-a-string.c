char* digitSum(char* s, int k) {
    char* current_s = strdup(s); // Duplicate the input string to work with
    
    while (strlen(current_s) > k) {
        char* next_s = (char*)malloc(sizeof(char) * (strlen(current_s) * 3 + 1)); // Allocate enough space for the new string (max sum of 99 * k digits)
        if (next_s == NULL) {
            // Handle allocation error
            free(current_s);
            return NULL;
        }
        next_s[0] = '\0'; // Initialize as an empty string

        int current_index = 0;
        int next_s_len = 0;

        while (current_index < strlen(current_s)) {
            int group_sum = 0;
            for (int i = 0; i < k && (current_index + i) < strlen(current_s); ++i) {
                group_sum += (current_s[current_index + i] - '0');
            }

            char temp_sum_str[10]; // Buffer to store the sum as a string
            sprintf(temp_sum_str, "%d", group_sum);
            
            strcat(next_s, temp_sum_str);
            next_s_len += strlen(temp_sum_str);
            
            current_index += k;
        }
        
        free(current_s); // Free the old string
        current_s = next_s; // Update current_s to the new string
    }
    
    return current_s; // Return the final string
}