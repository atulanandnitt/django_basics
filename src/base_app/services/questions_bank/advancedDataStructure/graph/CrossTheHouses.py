# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 15:16:30 2018

@author: atanand
"""

import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

class cell:{
	public int row;
	public int column;
	public cell(int row, int column){
		this.row=row;
		this.column=column;
	}
	
}
public class CrossTheHouses {
	
	public int stepCount=-1;
	
	public void bfs(char[][] arr, int rowLen, int colLen){
		boolean[][] visited=new boolean[rowLen][colLen];
		
		cell start=new cell(0,0);
		cell dest = new cell(0,0);
		for(int i=0;i<rowLen;i++){
			for(int j=0;j<colLen;j++){
				if(arr[i][j]=='M')
					start=new cell(i,j);
				if(arr[i][j]=='P')
					dest=new cell(i,j);
				visited[i][j]=false;
			}
		}
		List<cell> visitedCells1=new LinkedList<>();
		List<cell> visitedCells2=new LinkedList<>();
		visitedCells1.add(start);
		int count=0;
		while(!visitedCells1.isEmpty()){
			cell newCell=visitedCells1.get(0);
			if(newCell.row==dest.row && newCell.column==dest.column){
				stepCount=count;
				return;
			}
			//System.out.println("Cell picked = "+newCell.row+" : "+newCell.column);	
			if(!visited[newCell.row][newCell.column]){
				visited[newCell.row][newCell.column]=true;
				if(newCell.row-1>=0 && !visited[newCell.row-1][newCell.column] && (arr[newCell.row-1][newCell.column]=='.' || arr[newCell.row-1][newCell.column]=='P')){
					visitedCells2.add(new cell(newCell.row-1, newCell.column));
				}
				if(newCell.column-1>=0 && !visited[newCell.row][newCell.column-1] && (arr[newCell.row][newCell.column-1]=='.' || arr[newCell.row][newCell.column-1]=='P')){
					visitedCells2.add(new cell(newCell.row, newCell.column-1));
				}
				if(newCell.row+1<rowLen && !visited[newCell.row+1][newCell.column] && (arr[newCell.row+1][newCell.column]=='.' || arr[newCell.row+1][newCell.column]=='P')){
					visitedCells2.add(new cell(newCell.row+1, newCell.column));
				}
				if(newCell.column+1<colLen && !visited[newCell.row][newCell.column+1] && (arr[newCell.row][newCell.column+1]=='.' || arr[newCell.row][newCell.column+1]=='P')){
					visitedCells2.add(new cell(newCell.row, newCell.column+1));
				}
			}
			
			visitedCells1.remove(0);
			if(visitedCells1.isEmpty()):{
				count++;
				visitedCells1.addAll(visitedCells2);
				visitedCells2.removeAll(visitedCells1);
			}
		}
		
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int rows=sc.nextInt();
		int cols=sc.nextInt();
		sc.nextLine();
		char[][] input=new char[rows][cols];
		for(int i=0;i<rows;i++){
			String in=sc.nextLine();
			for(int j=0;j<cols;j++)
				input[i][j]=in.charAt(j);
		}
		CrossTheHouses cth=new CrossTheHouses();
				cth.bfs(input, rows, cols);
		System.out.println(cth.stepCount);
	}

}
