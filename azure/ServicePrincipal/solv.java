public class Program
{
  public static void Main(string[] args)
  {
      CreateHostBuilder(args).Build().Run();
  }

  public static IHostBuilder CreateHostBuilder(string[] args) =>
      Host.CreateDefaultBuilder(args)
          .ConfigureAppConfiguration((context, config) =>
          {
              var keyVaultEndpoint = GetKeyVaultEndpoint();
              if (!string.IsNullOrEmpty(keyVaultEndpoint))
              {
                  // In below connection string, replace
                  // {ClientId} with actual GUID representing client id 
                  // {TenantId} with tenant id of Azure AD\
                  // {ClientSecret} with the client secret you generated
                  var connectionString = "RunAs=App;AppId=638ba534-d2ee-475a-adf7-089190310ec0;TenantId=6837db8b-72d9-4346-bbb4-c2536150adf5;AppKey=ab28Q~u1z~KktYhXgfAn4OwTFtYv.NsojE4GlcO~}";
                  
                  var azureServiceTokenProvider = new AzureServiceTokenProvider(connectionString);
                  var keyVaultClient = new KeyVaultClient(
                      new KeyVaultClient.AuthenticationCallback(
                          azureServiceTokenProvider.KeyVaultTokenCallback));
                  config.AddAzureKeyVault(keyVaultEndpoint, keyVaultClient, new DefaultKeyVaultSecretManager());
              }
          })
          .ConfigureWebHostDefaults(webBuilder =>
          {
              webBuilder.UseStartup<Startup>();
          });

  private static string GetKeyVaultEndpoint() => "https://<<your-key-vault>>.vault.azure.net";
}