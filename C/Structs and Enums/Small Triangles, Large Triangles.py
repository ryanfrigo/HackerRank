

void swap(triangle *a, triangle *b) {
  triangle temp = *a;
  *a = *b;
  *b = temp;
}
int heron(triangle tr) {
  int a = tr.a;
  int b = tr.b;
  int c = tr.c;
  int p = (a + b + c) / 2;
  return (a + b + c) * (a - b + c) * (a + b - c) * (-a + b + c);
}
void sort_by_area(triangle *tr, int n) {
  /**
   * Sort an array a of the length n
   */
  for (int i = 0; i < n; i++) {
    int sorted = 1;
    for (int j = 0; j < n - i - 1; j++) {
      if (heron(tr[j]) > heron(tr[j + 1]))
        swap(&tr[j], &tr[j + 1]);
      sorted = 0;
    }
    if (sorted == 1)
      break;
  }
}

