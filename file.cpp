#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <stdio.h>
#include <string>

using namespace std;

void do_cpp_file() {
  cout << "do_cpp_file() " << endl;
  fstream file;
  file.open("test.txt");

  string line;
  while(getline(file, line)) {
    unsigned long number;
    line.erase(std::find(line.begin(), line.end(), ' '), line.end());
    cout << line.size() << endl;
    istringstream(line) >> std::hex >> number;
    cout << hex << number << endl;
  }

  file.close();
  cout << "do_cpp_file() " << endl;
}

void do_c_file() {
  cout << "do_c_file() " << endl;
  FILE* fp = fopen("test.txt", "r");
  char line [512];
  while(fgets(line, 512, fp)) {
    unsigned long number;
    string string_num;
    //istringstream(line) >> std::hex >> number;
    istringstream(line) >> std::hex >> string_num;
    cout << string_num << " : " << string_num.size() << endl;
    for(int i =string_num.size()-16; i > 0; i-=16)
    {
      cout << string_num.substr(i,16) << endl;
    }
    //size_t pos = 0;
    //number = stoul(string_num, &pos, 16);
    //cout << stoul(string_num, 0, 16) << endl;
    cout << hex << number << " " <<  endl;
  }
  cout << "do_c_file() " << endl;
}

void do_s_file() {
  cout << "do_s_file() " << endl;
  FILE* fp = fopen("test.txt", "r");
  char line [512];
  while(fgets(line, 512, fp)) {
    unsigned long number;
    string string_num;
    istringstream st;
    istringstream(line) >> st;
    int offset = st.end > 16 ? -16 : -st.end;
    st.seekg(offset, st.end);
    cout << std::dec << st.tellg() << endl; 
    st >> std::hex >> number;
    //cout << string_num << " : " << string_num.size() << endl;
    cout << std::hex << number << endl;

    //istringstream st = istringstream(string_num);
    //int str[20];
    //st.get(str, 20);
    //cout << str << endl;
    //cout << st.tellg() << endl; 
    //st.seekg(-4, st.end);
    //cout << st.tellg() << endl; 
    //st.read(number, 4);
    //cout << std::hex << number << endl;
    //>> std::hex >> data;
    //basic_stringstream<long long int>(line) >> num_arr[0];
    //cout << num_arr[0] << endl;
    //size_t pos = 0;
    //number = stoul(string_num, &pos, 16);
    //cout << stoul(string_num, 0, 16) << endl;
    //cout << hex << number << " " <<  endl;
  }
  cout << "do_s_file() " << endl;
}

int main () {
  cout << sizeof(long long int) << endl;
  //do_cpp_file();
  do_s_file();

  return 0;
}
