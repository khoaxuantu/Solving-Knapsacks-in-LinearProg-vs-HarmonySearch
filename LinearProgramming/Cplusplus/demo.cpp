#include <iostream>
#include <vector>

#include "absl/flags/flag.h"
#include "ortools/base/init_google.h"
#include "ortools/base/logging.h"
#include "ortools/base/logging_flags.h"
#include "ortools/linear_solver/linear_solver.h"

#define ITEMS_NUM 5

using namespace std;
using namespace operations_research;

/*
	Items = 5
			[1, 2, 3, 4, 5]
	Value = [3, 6, 5, 10, 8]
	Weight = [2, 7, 1, 3, 4]
*/
vector<int> value = {3, 6, 5, 10, 8};
vector<int> weight = { 2, 7, 1, 3, 4 };

void LPsolving()
{
	unique_ptr<MPSolver> solver(MPSolver::CreateSolver("GLOP"));
	if (!solver)
	{
		LOG(WARNING) << "GLOP is not available.";
		return;
	}

	const double infinity = solver->infinity();
	// Non-negative variables

}

int main()
{
	
}