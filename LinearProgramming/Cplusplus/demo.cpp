#include <iostream>
#include <vector>

#include "ortools/linear_solver/linear_solver.h"

#define ITEMS_NUM 5
#define MAX_WEIGHT 250

using namespace std;
using namespace operations_research;

/*
	Items = 5
			[1, 2, 3, 4, 5]
	Value = [3, 6, 5, 10, 8]
	Weight = [2, 7, 1, 3, 4]
*/
//vector<int> value = {3, 6, 5, 10, 8};
//vector<int> weight = { 2, 7, 1, 3, 4 };

// Constuct item structure
struct Item
{
	string name;
	double value;
	double weight;
};

void LPsolving()
{
	// Construct a list of items
	vector<Item> itemList = {
		{"item 1", 3 , 2},
		{"item 2", 6 , 7},
		{"item 3", 5 , 1},
		{"item 4", 10, 3},
		{"item 5", 8 , 4}
	};

	unique_ptr<MPSolver> solver(MPSolver::CreateSolver("GLOP"));
	if (!solver)
	{
		LOG(WARNING) << "GLOP is not available.";
		return;
	}

	// Define the variables
	const double infinity = solver->infinity();
	// Non-negative variables
	vector<const MPVariable*> x(ITEMS_NUM);
	for (const Item& item : itemList)
	{
		x.push_back(solver->MakeNumVar(0.0, infinity, item.name));
	}
	LOG(INFO) << "Number of variables: " << solver->NumVariables();

	// Define the constraints
	MPConstraint* constraint = solver->MakeRowConstraint(0, MAX_WEIGHT);
	for (int i = 0; i < ITEMS_NUM; i++)
	{
		constraint->SetCoefficient(x[i], itemList[i].weight);
	}
	LOG(INFO) << "Number of constraints = " << solver->NumConstraints();

	// Create the objective function
	MPObjective* const obj = solver->MutableObjective();
	for (int i = 0; i < ITEMS_NUM; i++)
	{
		obj->SetCoefficient(x[i], itemList[i].value);
	}
	obj->SetMaximization();

	// Display the solution
	const MPSolver::ResultStatus result_status = solver->Solve();
	// If the solution is infeasible
	if (result_status != MPSolver::OPTIMAL)
	{
		LOG(FATAL) << "The problem does not have an optimal solution.";
	}

	LOG(INFO) << "Solution: ";
	LOG(INFO) << "Optimal objective value = " << obj->Value();

	// Display number of items needed
	for (int i = 0; i < ITEMS_NUM; i++)
	{
		LOG(INFO) << "Item " << i + 1 << " = " << x[i]->solution_value();
	}
}

int main()
{
	LPsolving();
}