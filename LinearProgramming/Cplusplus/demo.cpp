#include <iostream>

#include "ortools/linear_solver/linear_solver.h"

#define ITEMS_NUM 5

using namespace std;

/*
	Items = 5
			[1, 2, 3, 4, 5]
	Value = [3, 6, 5, 10, 8]
	Weight = [2, 7, 1, 3, 4]
*/

void LPsolving()
{
	unique_ptr<MPSolver> solver(MPSolver::CreateSolver("SCIP"));
	if (!solver)
	{
		LOG(WARNING) << "SCIP is not available.";
		return;
	}

	const double infinity = solver->infinity();
	// Non-negative variables

}

int main()
{
	
}