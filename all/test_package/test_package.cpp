#include "durak_computer_controlled_opponent/simulation/compressCard.hxx"
#include "durak_computer_controlled_opponent/simulation/permutation.hxx"

int main() {
  auto const result = durak_computer_controlled_opponent::compress ({ { 6, durak::Type::clubs }, { 11, durak::Type::clubs }, { 14, durak::Type::clubs }, { 8, durak::Type::hearts } });
  auto const desire = std::vector<durak::Card>{ { 0, durak::Type::clubs }, { 2, durak::Type::clubs }, { 3, durak::Type::clubs }, { 1, durak::Type::hearts } };
  if (result != desire)
  {
    std::terminate();
  }
  return 0;
}
