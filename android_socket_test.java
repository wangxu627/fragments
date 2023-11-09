package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class SecondActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);

        connectToServer("localhost", 8890);
    }

    public void connectToServer(String serverIp, int serverPort) {
        // 在合适的地方执行 MyTask 异步任务
//        MyTask myTask = new MyTask();
//        myTask.execute(); // 启动异步任务


        // 创建一个单线程池，用于执行网络操作
        ExecutorService executorService = Executors.newSingleThreadExecutor();

        // 执行网络操作并获取结果
        Future<String> future = executorService.submit(new Callable<String>() {
            @Override
            public String call() throws Exception {
                return performNetworkOperation();
            }
        });

        // 在UI线程中处理结果
        try {
            String result = future.get(); // 阻塞等待获取结果
            int i = 100;
//            resultTextView.setText("服务器响应: " + result);
            Log.d("TAG", "服务器响应: " + result);
        } catch (Exception e) {
            e.printStackTrace();
        }

        // 关闭线程池
        executorService.shutdown();
    }

    private String performNetworkOperation() {
        try {
            String serverIp = "10.196.10.21"; // 替换成你的主机IP地址
            int serverPort = 8991;

            Socket socket = new Socket(serverIp, serverPort);

            String message = "Hello";
            OutputStream outputStream = socket.getOutputStream();
            outputStream.write(message.getBytes());

            BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
//            String response = reader.readLine();
//            char buffer[] = new char[1024];
//            reader.read(buffer, 0, 1024);
            StringBuilder stringBuilder = new StringBuilder();
            char[] buffer = new char[1024]; // 用于存储读取的字符
            int bytesRead;
//            while ((bytesRead = reader.read(buffer)) != -1) {
            bytesRead = reader.read(buffer);
            stringBuilder.append(buffer, 0, bytesRead);
//            }
            String receivedData = stringBuilder.toString();
            socket.close();

            Log.d("TAG", receivedData);
            return receivedData;
        } catch (IOException e) {
            e.printStackTrace();
            return "网络操作失败";
        }
    }
}
