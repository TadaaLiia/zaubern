import de.businesscode.batch.core.Batch;

public class SetupZauberDB extends Batch {
  @Override
  public void implementMain(String[] arguments) throws Exception {
    
	  double step = 0.0;
	  
	  addSqlFileStep("player", step++);  
	  addSqlFileStep("game", step++);  
	  
    System.out.println("implement main executed");
  }
  
  public static void main(String[] args) {
    new SetupZauberDB().doMain(args); // dispatch do engine implementation
  }
}
