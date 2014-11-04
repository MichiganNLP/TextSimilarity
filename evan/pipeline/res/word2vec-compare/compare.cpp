//  Copyright 2013 Google Inc. All Rights Reserved.
//
//  Licensed under the Apache License, Version 2.0 (the "License");
//  you may not use this file except in compliance with the License.
//  You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
//  Unless required by applicable law or agreed to in writing, software
//  distributed under the License is distributed on an "AS IS" BASIS,
//  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//  See the License for the specific language governing permissions and
//  limitations under the License.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <malloc.h>
#include <ctype.h>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
using namespace std;

const long long max_size = 2000;         // max length of strings
const long long N = 1;                   // number of closest words
const long long max_w = 50;              // max length of vocabulary entries

double cosine_similarity(float* a, float* b, long long size) {
  cout << "computing similarity..." << endl;
  long long i;
  double numerator = 0;
  double denominator;
  float a_squared = 0;
  float b_squared = 0;
  for (i = 0; i < size; i ++) {
    cout << "i = " << i << endl;
    numerator += a[i] * b[i];
    a_squared += (a[i] * a[i]);
    b_squared += (b[i] * b[i]);
  }
  denominator = sqrt(a_squared) * sqrt(b_squared);
  return numerator / denominator;
}

int main(int argc, char **argv) {

  FILE *f;
  ifstream compare_file(argv[2]);
  char file_name[max_size];
  float len;
  long long num_words, vector_size;
  map<string, float*> vocab;

  if (argc < 3) {
    printf("Usage: ./compare <VECTORS> <TOCOMPARE>\nwhere VECTORS contains word projections and TOCOMPARE contains pairs of words\n");
    return 0;
  }

  strcpy(file_name, argv[1]);
  f = fopen(file_name, "rb");
  if (f == NULL) {
    printf("Input file not found\n");
    return -1;
  }
  fscanf(f, "%lld", &num_words);
  fscanf(f, "%lld", &vector_size);

  cout << "There are " << num_words << " words. ";
  cout << "Each vector is of size " << vector_size << "." << endl;

  for (long long i = 0; i < num_words; i++) {

    string tmp_word = "";
    while (1) {
      char tmp_char = toupper(fgetc(f));
      cout << tmp_char;
      if ((feof(f)) ||
          (tmp_char == ' ') ||
          (tmp_char == '\n')) {
        break;
      }
      tmp_word += tmp_char;
    }

    /*
    vocab[tmp_word] = (float*)malloc(vector_size * sizeof(float));
    if (vocab[tmp_word] == NULL) {
      printf("Cannot allocate memory: %lld MB\n", vector_size * sizeof(float) / 1048576);
      return -1;
    }
    */

    /*
    for (long long i = 0; i < vector_size; i ++) {
      float to_add;
      fread(&to_add, sizeof(float), 1, f);
      vocab[tmp_word][i] = to_add;
      cout << tmp_word << ": " << i << ": " << to_add << endl;
      // fread(&vocab[tmp_word][i], sizeof(float), 1, f);
    }
    */

    /*
    len = 0;
    for (a = 0; a < size; a++) len += vocab[tmp_word][a] * vocab[tmp_word][a];
    len = sqrt(len);
    for (a = 0; a < size; a++) vocab[tmp_word][a] /= len;
    */
  }
  fclose(f);
  return 0;

  while (!compare_file.eof()) {

    string word_a;
    string word_b;
    compare_file >> word_a;
    compare_file >> word_b;
    if (!word_a.size()) break;

    float* word_a_vector = vocab[word_a];
    float* word_b_vector = vocab[word_b];

    for (long long i = 0; i < vector_size; i ++) {
      cout << word_a_vector[i] << endl;
    }

    /* double similarity = cosine_similarity(word_a_vector, word_b_vector, size); */
    /* cout << "similarity = " << similarity << endl; */

  }

  /*

  TCN = 0;
  while (1) {
    for (a = 0; a < N; a++) bestd[a] = 0;
    for (a = 0; a < N; a++) bestw[a][0] = 0;
    scanf("%s", st1);
    for (a = 0; a < strlen(st1); a++) st1[a] = toupper(st1[a]);
    if ((!strcmp(st1, ":")) || (!strcmp(st1, "EXIT")) || feof(stdin)) {
      if (TCN == 0) TCN = 1;
      if (QID != 0) {
        printf("ACCURACY TOP1: %.2f %%  (%d / %d)\n", CCN / (float)TCN * 100, CCN, TCN);
        printf("Total accuracy: %.2f %%   Semantic accuracy: %.2f %%   Syntactic accuracy: %.2f %% \n", CACN / (float)TACN * 100, SEAC / (float)SECN * 100, SYAC / (float)SYCN * 100);
      }
      QID++;
      scanf("%s", st1);
      if (feof(stdin)) break;
      printf("%s:\n", st1);
      TCN = 0;
      CCN = 0;
      continue;
    }
    if (!strcmp(st1, "EXIT")) break;
    scanf("%s", st2);
    for (a = 0; a < strlen(st2); a++) st2[a] = toupper(st2[a]);
    scanf("%s", st3);
    for (a = 0; a<strlen(st3); a++) st3[a] = toupper(st3[a]);
    scanf("%s", st4);
    for (a = 0; a < strlen(st4); a++) st4[a] = toupper(st4[a]);
    for (b = 0; b < words; b++) if (!strcmp(&vocab[b * max_w], st1)) break;
    b1 = b;
    for (b = 0; b < words; b++) if (!strcmp(&vocab[b * max_w], st2)) break;
    b2 = b;
    for (b = 0; b < words; b++) if (!strcmp(&vocab[b * max_w], st3)) break;
    b3 = b;
    for (a = 0; a < N; a++) bestd[a] = 0;
    for (a = 0; a < N; a++) bestw[a][0] = 0;
    TQ++;
    if (b1 == words) continue;
    if (b2 == words) continue;
    if (b3 == words) continue;
    for (b = 0; b < words; b++) if (!strcmp(&vocab[b * max_w], st4)) break;
    if (b == words) continue;
    for (a = 0; a < size; a++) vec[a] = (M[a + b2 * size] - M[a + b1 * size]) + M[a + b3 * size];
    TQS++;
    for (c = 0; c < words; c++) {
      if (c == b1) continue;
      if (c == b2) continue;
      if (c == b3) continue;
      dist = 0;
      for (a = 0; a < size; a++) dist += vec[a] * M[a + c * size];
      for (a = 0; a < N; a++) {
        if (dist > bestd[a]) {
          for (d = N - 1; d > a; d--) {
            bestd[d] = bestd[d - 1];
            strcpy(bestw[d], bestw[d - 1]);
          }
          bestd[a] = dist;
          strcpy(bestw[a], &vocab[c * max_w]);
          break;
        }
      }
    }
    if (!strcmp(st4, bestw[0])) {
      CCN++;
      CACN++;
      if (QID <= 5) SEAC++; else SYAC++;
    }
    if (QID <= 5) SECN++; else SYCN++;
    TCN++;
    TACN++;
  }
  printf("Questions seen / total: %d %d   %.2f %% \n", TQS, TQ, TQS/(float)TQ*100);
  */
  return 0;
}
